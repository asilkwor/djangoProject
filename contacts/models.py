# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL
# Create your models here.
class Contact(models.Model):
	user		 = models.ForeignKey(User)
	first_Name   = models.CharField(max_length=120)
	last_Name    = models.CharField(max_length=120, blank=True,null=False)
	phone_number = models.CharField(max_length=12, blank=True,null=False)
	address      = models.CharField(max_length=120, blank=True,null=False)
	email        = models.EmailField(max_length=120, blank=True,null=False)
	description  = models.CharField(max_length=200, blank=True,null=False)


	def get_absolute_url(self):
		return reverse("contacts:contact-detail", kwargs={"id": self.id})