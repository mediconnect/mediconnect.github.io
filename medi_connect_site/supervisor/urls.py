from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from supervisor import views as supervisor_views

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'supervisor_login.html'}, name='supervisor_login'),
    url(r'^home/(?P<id>\d+)/',supervisor_views.supervisor, name = 'supervisor_home'),
    url(r'^logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^detail/(?P<id>\d+)/',supervisor_views.trans_signup ,name = 'trans_signup'),
    url(r'^trans_signup/(?P<id>\d+)/',supervisor_views.detail ,name = 'detail'),
    url(r'^customer_list',supervisor_views.cutomer_list,name = 'customer_list'),
    url(r'^translator_list',supervisor_views.translator_list,name = 'translator_list')
]
