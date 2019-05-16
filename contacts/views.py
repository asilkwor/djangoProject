# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect

from django.shortcuts import redirect, render_to_response

from django.shortcuts import render, get_object_or_404, redirect

from django.db.models.functions import Concat

from django.db.models import Q, Value as V

from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
)
from .forms import ContactModelForm
from .models import Contact

class ContactCreateView(LoginRequiredMixin, CreateView):
	form_class = ContactModelForm
	template_name= 'contact_create.html'
	queryset = Contact.objects.all()
	success_url = '/contact/list'
	login_url = '/login'

	def form_valid(self, form):
		user = self.request.user
		form.instance.user = user
		return super(ContactCreateView, self).form_valid(form)

class ContactListView(LoginRequiredMixin, ListView):
	template_name='contact_list.html'
	queryset = Contact.objects.all()
	login_url = '/login'

	def get_queryset(self):
		q = self.request.GET.get('q')
		f = self.request.GET.get('f')
		l = self.request.GET.get('l')
		if q is not None:
			if f is not None:
				return Contact.objects.annotate(full_name=Concat('first_Name', V(' '), 'last_Name')).filter(user=self.request.user, full_name__icontains=q).order_by('first_Name')
			elif l is not None:
				return Contact.objects.annotate(full_name=Concat('first_Name', V(' '), 'last_Name')).filter(user=self.request.user, full_name__icontains=q).order_by('last_Name')
			else:
				return Contact.objects.annotate(full_name=Concat('first_Name', V(' '), 'last_Name')).filter(user=self.request.user, full_name__icontains=q)
		elif f is not None:
			return Contact.objects.filter(user=self.request.user).order_by('first_Name')
		elif l is not None:
			return Contact.objects.filter(user=self.request.user).order_by('last_Name')
		else:
			return Contact.objects.filter(user=self.request.user)

class ContactDetailView(LoginRequiredMixin, DetailView):
	template_name= 'contact_detail.html'
	queryset = Contact.objects.all()
	login_url = '/login'

	def get_object(self, *args, **kwargs):
		id = self.kwargs.get("id")
		obj = Contact.objects.get(id=id) 
		username = self.request.user
		if username == obj.user:
			return get_object_or_404(Contact, id=id )
		else: 
			return render_to_response('Only valid users can view this Contact')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
	form_class = ContactModelForm
	template_name= 'contact_update.html'
	queryset = Contact.objects.all()
	success_url = '/contact/list'
	login_url = '/login'

	def get_object(self):
		id = self.kwargs.get("id")
		obj = Contact.objects.get(id=id) 
		username = self.request.user
		if username == obj.user:
			return get_object_or_404(Contact, id=id )
		else: 
			return render_to_response('Only valid users can view this Contact')

	def form_valid(self, form):
		user = self.request.user
		form.instance.user = user
		return super(ContactUpdateView, self).form_valid(form)

class ContactDeleteView(LoginRequiredMixin, DeleteView):
	template_name= 'contact_delete.html'
	queryset = Contact.objects.all()
	success_url = '/contact/list'
	login_url = '/login'

	def get_object(self):
		id = self.kwargs.get("id")
		obj = Contact.objects.get(id=id) 
		username = self.request.user
		if username == obj.user:
			return get_object_or_404(Contact, id=id )
		else: 
			return render_to_response('Only valid users can view this Contact')