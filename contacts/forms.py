from django import forms 

from .models import Contact

class ContactModelForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
	'first_Name',
	'last_Name',   
	'phone_number', 
	'address',      
	 'email',        
	'description'


		]