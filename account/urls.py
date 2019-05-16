from django.conf.urls import url

from .views import register, register_fail

app_name= 'account'

urlpatterns = [

    url(r'^register/$', register, name='account-register'),
    url(r'^register/fail/$', register_fail, name='account-register_fail'),
]