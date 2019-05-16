# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			new_user=form.save()
			login(request, new_user)
			return redirect('/contact/list')
		else: 
			return redirect('/account/register/fail')
	else:
		form = UserCreationForm()

		args = {'form': form}
		return render(request, 'account_register.html', args)

def register_fail(request):
	if request.method=='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			new_user=form.save()
			login(request, new_user)
			return redirect('/contact/list')
		else: 
			return redirect('/account/register/fail')
	else:
		form = UserCreationForm()

		args = {'form': form}
		return render(request, 'account_register_fail.html', args)