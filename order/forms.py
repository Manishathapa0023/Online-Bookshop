from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):

	DIVISION_CHOICES = (
		('Provience-1', 'Provience-1'), 
		('Provience-2', 'Provience-2'),
		('Provience-3', 'Provience-3'),
		('Provience-4', 'Provience-4'),
		('Provience-5', 'Provience-5'),
		('Provience-6', 'Provience-6'),
		('Provience-7', 'Provience-7'),
	)

	DISCRICT_CHOICES = (

		('Bhojpur', 'Bhojpur'),
		('Dhankuta', 'Dhankuta'),
		('Ilam', 'Ilam'),
		('Jhapa', 'Jhapa'),
		('Khotang', 'Khotang'),
		('Morang', 'Morang'),
		('Panchthar', 'Panchthar'),
		('Solukhumbu', 'Solukhumbu'),
		('Sunsari', 'Sunsari'),
		('Udayapur', 'Udayapur'),

	)
	PAYMENT_CHOICES = (
		('E- Sewa', 'E-Sewa'), 
		('Khalti', 'Khalti'), 
		('Connect-IPS', 'Connect-IPS'), 
		
	)
	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES)


	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code','payment_method','account_number']

	widgets = {
            'payment_method': forms.TextInput(attrs={'required': False}),
			'account_number': forms.TextInput(attrs={'required': False}),
        }
