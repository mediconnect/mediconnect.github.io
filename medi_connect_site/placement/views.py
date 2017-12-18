from django.shortcuts import render, redirect
from django.http import JsonResponse
from helper.models import Hospital, Patient, Disease, Order, Document, HospitalReview, LikeHospital, OrderPatient, Rank, Slot
from customer.models import Customer
from django.contrib.auth.decorators import login_required
from helper.forms import PatientInfo, AppointmentInfo
from helper.models import auto_assign
from dynamic_form.forms import create_form, get_fields
from django.core.paginator import Paginator, EmptyPage
import datetime
import calendar
from time import sleep
from threading import Thread
import pytz


@login_required
def hospital_detail(request, hospital_id, disease_id):
    hosp = Hospital.objects.get(id=hospital_id)
    dis = Disease.objects.get(id=disease_id)
    customer = Customer.objects.get(user=request.user)
    order_list = Order.objects.filter(customer=customer, hospital=hosp, disease=dis)
    order = None
    for each in order_list:
        if int(each.status) == 0:
            order = each
            break
    order = Order(hospital=hosp, status=0, disease=dis, customer=customer) if order is None else order
    order.save()
    slot = Slot.objects.get(hospital=hosp, disease=dis)
    slots = {0: slot.slots_open_0, 1: slot.slots_open_1, 2: slot.slots_open_2, 3: slot.slots_open_3}
    comments = HospitalReview.objects.filter(hospital=hosp)
    pages = Paginator(comments, 2)
    try:
        comments = pages.page(1)
    except EmptyPage:
        comments = False

    # start thread for 5 minutes order cleaning
    Thread(target=clean_order, args=(order.id,)).start()
    return render(request, "hospital_order.html", {
        'hospital': hosp,
        'rank': Rank.objects.get(disease=dis, hospital=hosp).rank,
        'slots': slots,
        'disease': dis,
        'customer': customer,
        'order_id': order.id,
        'comments': comments,
    })


def clean_order(order_id):
    order = Order.objects.get(id=order_id)
    if order is None:
        return
    while True:
        if int(order.status) > 1:
            break
        naive = order.submit
        diff = datetime.datetime.now(tz=pytz.utc) - naive
        if diff.total_seconds() / 60 > 5:
            if order.week_number_at_submit != 0:
                if slot_num == 0:
                    slot.slots_open_0 += 1
                elif slot_num == 1:
                    slot.slots_open_1 += 1
                elif slot_num == 2:
                    slot.slots_open_2 += 1
                else:
                    slot.slots_open_3 += 1
            order.delete()
            break
        sleep(60)


@login_required
def get_comment(request):
    hospital_id = int(request.GET.get('hospital_id', None))
    page = int(request.GET.get('page', None))
    hosp = Hospital.objects.get(id=hospital_id)
    comments = HospitalReview.objects.filter(hospital=hosp)
    pages = Paginator(comments, 2)

    try:
        comments = pages.page(page + 1)
    except EmptyPage:
        comments = None

    if comments is None:
        return JsonResponse({'status': 'empty'})

    data = dict()
    data['comments'] = [x.comment for x in comments]
    data['status'] = 'exist'
    return JsonResponse(data)


@login_required
def fast_order(request, disease_id, hospital_id, slot_num):
    """
    Handle order request with entering hospital detail page.
    """
    hosp = Hospital.objects.get(id=hospital_id)
    dis = Disease.objects.get(id=disease_id)
    customer = Customer.objects.get(user=request.user)
    order_list = Order.objects.filter(customer=customer, hospital=hosp, disease=dis)
    order = None
    for each in order_list:
        if int(each.status) == 0:
            order = each
            break
    order = Order(hospital=hosp, status=0, disease=dis, customer=customer) if order is None else order
    order.save()
    return redirect('order_info_first', order_id=order.id, slot_num=int(slot_num))


@login_required
def order_info_first(request, order_id, slot_num):
    customer = Customer.objects.get(user=request.user)
    order = Order.objects.get(id=order_id)
    order.customer = customer
    order.status = 0
    hosp = order.hospital
    slot_num = int(slot_num)
    slot = Slot.objects.get(disease=order.disease, hospital=order.hospital)
    # check if order chosen slot before
    if order.week_number_at_submit != 0:
        if slot_num == 0:
            slot.slots_open_0 += 1
        elif slot_num == 1:
            slot.slots_open_1 += 1
        elif slot_num == 2:
            slot.slots_open_2 += 1
        else:
            slot.slots_open_3 += 1
    order.week_number_at_submit = slot_num
    order.save()
    avail_slot = {
        0: slot.slots_open_0,
        1: slot.slots_open_1,
        2: slot.slots_open_2,
        3: slot.slots_open_3,
    }[slot_num]
    if avail_slot < 1:
        return render(request, "hospital_order.html", {
            'hospital': hosp,
            'customer': customer,
            'order_id': order.id,
            'error': 'the hospital does not have available slot'
        })
    if slot_num == 0:
        slot.slots_open_0 -= 1
    elif slot_num == 1:
        slot.slots_open_1 -= 1
    elif slot_num == 2:
        slot.slots_open_2 -= 1
    else:
        slot.slots_open_3 -= 1
    slot.save()
    pin_yin = order.patient_order.pin_yin.split() if order.patient_order is not None and len(order.patient_order.pin_yin) >= 3 else ['', '']
    return render(request, 'order_info_first.html', {
        'customer': customer,
        'form': PatientInfo(instance=request.user, initial={
            'contact': customer.get_name(),
            'email': customer.user.email,
            'address': customer.address,
            'telephone': customer.tel,
            'wechat': customer.wechat if len(customer.wechat) >= 1 else 'unknown',
            'qq': customer.qq if len(customer.qq) >= 1 else 'unknown',
            'first_name': order.patient_order.first_name if order.patient_order is not None else '',
            'last_name': order.patient_order.last_name if order.patient_order is not None else '',
            'birth': order.patient_order.birth if order.patient_order is not None else '',
            'gender': order.patient_order.gender if order.patient_order is not None else '',
            'relationship': order.patient_order.relationship if order.patient_order is not None else '',
            'passport': order.patient_order.passport if order.patient_order is not None else '',
            'first_name_pin_yin': pin_yin[0],
            'last_name_pin_yin': pin_yin[1],
        }),
        'order_id': order.id,
        'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
    })


@login_required
def order_submit_first(request, order_id):
    if request.method == 'POST':
        form = PatientInfo(request.POST)
        order = Order.objects.get(id=order_id)
        customer = Customer.objects.get(user=request.user)
        if not form.is_valid():
            return render(request, 'order_info_first.html', {
                'form': form,
                'order_id': order.id,
                'customer': customer,
                'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
            })
        else:
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            birth = form.cleaned_data.get('birth')
            gender = form.cleaned_data.get('gender')
            relationship = form.cleaned_data.get('relationship')
            passport = form.cleaned_data.get('passport')
            first_name_pin_yin = form.cleaned_data.get('first_name_pin_yin')
            last_name_pin_yin = form.cleaned_data.get('last_name_pin_yin')
            # create patient or fetch accordingly
            patient = Patient() if order.patient is None else order.patient
            patient.customer = customer
            patient.first_name = first_name
            patient.last_name = last_name
            patient.birth = birth
            patient.gender = gender
            patient.relationship = relationship
            patient.passport = passport
            patient.pin_yin = first_name_pin_yin + ' ' + last_name_pin_yin
            patient.save()
            order.patient = patient

            order.status = 0

            order_patient = OrderPatient() if order.patient_order is None else order.patient_order
            order_patient.first_name = first_name
            order_patient.last_name = last_name
            order_patient.birth = birth
            order_patient.gender = gender
            order_patient.relationship = relationship
            order_patient.passport = passport
            order_patient.pin_yin = first_name_pin_yin + ' ' + last_name_pin_yin
            order_patient.save()
            order.patient_order = order_patient

            order.save()
            appointment_form = AppointmentInfo(instance=customer, initial={
                'hospital': order.hospital.name,
                'hospital_address': order.hospital.area,
                'time': order.submit,
                'name': order.disease.name,
                'diagnose_hospital': order.patient_order.diagnose_hospital if order.patient_order is not None else '',
                'doctor': order.patient_order.doctor if order.patient_order is not None else '',
                'contact': order.patient_order.contact if order.patient_order is not None else '',
            })
            form = create_form(int(order.hospital.id), int(order.disease.id), appointment_form)
            return render(request, 'order_info_second.html', {
                'customer': customer,
                'form': form,
                'order_id': order.id,
                'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
            })
    else:
        customer = Customer.objects.get(user=request.user)
        order = Order.objects.get(id=order_id)
        appointment_form = AppointmentInfo(instance=customer, initial={
            'hospital': order.hospital.name,
            'hospital_address': order.hospital.area,
            'time': order.submit,
            'name': order.disease.name,
            'diagnose_hospital': order.patient_order.diagnose_hospital if order.patient_order is not None else '',
            'doctor': order.patient_order.doctor if order.patient_order is not None else '',
            'contact': order.patient_order.contact if order.patient_order is not None else '',
        })
        form = create_form(int(order.hospital.id), int(order.disease.id), appointment_form)
        return render(request, 'order_info_second.html', {
            'customer': customer,
            'form': form,
            'order_id': order_id,
            'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
        })


@login_required
def order_patient_select(request, order_id):
    customer = Customer.objects.get(user=request.user)
    order = Order.objects.get(id=order_id)
    patients = Patient.objects.filter(customer=customer)
    return render(request, 'order_patient_select.html', {
        'customer': customer,
        'order_id': order.id,
        'patients': patients,
        'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
    })


@login_required
def order_patient_finish(request, order_id, patient_id):
    customer = Customer.objects.get(user=request.user)
    order = Order.objects.get(id=order_id)
    patient = Patient.objects.get(id=patient_id)
    order.patient = patient
    order_patient = OrderPatient(first_name=patient.first_name, last_name=patient.last_name, birth=patient.birth,
                                 gender=patient.gender, relationship=patient.relationship, passport=patient.passport,
                                 contact=patient.contact)
    order_patient.save()
    order.patient_order = order_patient
    order.save()
    appointment_form = AppointmentInfo(instance=customer, initial={
        'hospital': order.hospital.name,
        'hospital_address': order.hospital.area,
        'time': order.submit,
        'name': order.disease.name,
        'diagnose_hospital': order.patient_order.diagnose_hospital if order.patient_order is not None else '',
        'doctor': order.patient_order.doctor if order.patient_order is not None else '',
        'contact': order.patient_order.contact if order.patient_order is not None else '',
    })
    form = create_form(int(order.hospital.id), int(order.disease.id), appointment_form)
    return render(request, 'order_info_second.html', {
        'customer': customer,
        'form': form,
        'order_id': order.id,
        'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
    })


@login_required
def order_submit_second(request, order_id):
    order = Order.objects.get(id=order_id)
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        form = AppointmentInfo(request.POST, request.FILES, instance=customer)
        if not form.is_valid():
            return render(request, 'order_info_second.html', {
                'form': form,
                'order_id': order.id,
                'customer': customer,
                'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
            })
        else:
            required, optional = get_fields(order.hospital.id, order.disease.id)
            for field in required:
                for f in request.FILES.getlist(field):
                    doc = Document(document=f, description=field, order=order)
                    doc.save()
                    order.origin.add(doc)
            for field in optional:
                for f in request.FILES.getlist(field):
                    doc = Document(document=f, description=field, order=order)
                    doc.save()
                    order.origin.add(doc)
            doctor = form.cleaned_data.get('doctor')
            hospital = form.cleaned_data.get('diagnose_hospital')
            contact = form.cleaned_data.get('contact')
            patient = order.patient_order
            patient.doctor = doctor
            patient.diagnose_hospital = hospital
            patient.contact = contact
            patient.save()
            order.save()
            return render(request, 'order_review.html', {
                'customer': customer,
                'order': order,
                'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
            })
    return render(request, 'order_review.html', {
        'customer': customer,
        'order': order,
        'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
    })


@login_required
def pay_deposit(request, order_id, amount=-1):
    customer = Customer.objects.get(user=request.user)
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        if int(amount) == -1:
            order.full_payment_paid = False
        else:
            order.full_payment_paid = True
        order.status = 2
        order.save()
        return redirect('order_finish', order_id=order.id)
    # noinspection PyInterpreter
    return render(request, 'order_deposit.html', {
        'order': order,
        'customer': customer,
        'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
    })


@login_required
def finish(request, order_id):
    order = Order.objects.get(id=order_id)
    customer = Customer.objects.get(user=request.user)
    auto_assign(order)
    return render(request, 'finish.html', {
        'customer': customer,
        'time': (datetime.datetime.now(tz=pytz.utc) - order.submit).total_seconds(),
    })


@login_required
def like_hospital(request):
    customer = Customer.objects.get(user=request.user)
    hospital_id = int(request.GET.get('hospital_id', None))
    disease_id = int(request.GET.get('disease_id', None))
    mark = True if request.GET.get('mark', 'false') == 'true' else False
    hosp = Hospital.objects.get(id=hospital_id)
    dis = Disease.objects.get(id=disease_id)
    data = LikeHospital.objects.filter(customer=customer, hospital=hosp, disease=dis)

    if not mark:
        return JsonResponse({'status': "liked"}) if len(data) > 0 else JsonResponse({'status': 'no'})

    if len(data) > 0:
        for item in data:
            item.delete()
        return JsonResponse({'status': 'no'})

    add = LikeHospital(customer=customer, hospital=hosp, disease=dis)
    add.save()
    return JsonResponse({'status': 'liked'})


@login_required
def order_check(request):
    order_id = request.GET.get('order_id', None)
    orders = Order.objects.filter(id=order_id)
    if len(orders) > 0:
        return JsonResponse({'exist': True})
    return JsonResponse({'exist': False})