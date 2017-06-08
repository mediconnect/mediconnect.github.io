from django import forms
from django.contrib.auth.models import User
from supervisor.models import Supervisor
from translator.models import Translator
from helper.models import Document, Order

class AssignForm(forms.ModelForm):

    document = forms.ModelChoiceField(queryset = Document.objects.all())
    translator = forms.ModelChoiceField(queryset = Translator.objects.all())

    class Meta:
        model = Document
        fields = ['id','translator']

    def __init__(self, *args, **kwargs):
        super(AssignForm,self).__init__(*args,**kwargs)
        #self.fields['id'].widget = forms.Select(choices = Document.objects.all())
        #self.fields['translator'].widget = forms.Select(choices = Translator.objects.all())

class ApproveForm(forms.ModelForm):
    document = forms.ModelChoiceField(queryset = Document.objects.all())
    comment = forms.CharField(label = 'Please comment on the document if not approved')
    class Meta:
        model = Document
        fields = ['approved']

class TransSignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm your password",
        required=True)

    class Meta:
        model = User
        exclude = ['last_login', 'date_joined']
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

	def __init__(self, *args, **kwargs):
		
		super(TransSignUpForm, self).__init__(*args, **kwargs)
		self.field_order = ['username','password','confirm_password','first_name','last_name','email']
		self.order_fields(self.field_order)
		self.fields['password'].widget = forms.PasswordInput()

    def clean(slef):
    	super(TransSignUpForm, self).clean()
    	password = self.cleaned_data.get('password')
    	confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(
                ['Passwords don\'t match']
            )
            self._errors['confirm_password'] = self.error_class(
                ['Passwords don\'t match']
            )

        return self.cleaned_data