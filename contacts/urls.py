from django.conf.urls import url

from .views import (
	ContactListView, 
	ContactDetailView, 
	ContactCreateView,  
	ContactUpdateView,
	ContactDeleteView
)

app_name= 'contacts'

urlpatterns = [

	url(r'^create/$', ContactCreateView.as_view(), name='contact-create'),
    url(r'^list/$', ContactListView.as_view(), name='contact-list'),
    url(r'^(?P<id>\d+)/$', ContactDetailView.as_view(), name='contact-detail'),
    url(r'^(?P<id>\d+)/update/$', ContactUpdateView.as_view(), name='contact-update'),
    url(r'^(?P<id>\d+)/delete/$', ContactDeleteView.as_view(), name='contact-delete'),
]