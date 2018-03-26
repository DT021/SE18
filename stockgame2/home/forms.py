from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as auth_User
from home.models import Asset

class SignUpForm(UserCreationForm):
	# username = forms.CharField(label='Your name', max_length=20)
	# password = forms.CharField(max_length=20)
	# conf_pwd = forms.CharField(max_length=20)
	# email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
	class Meta:
		model = auth_User
		fields = ('username', 'password1', 'password2', 'email')

class BuyForm(forms.Form):
	ticker = forms.CharField(max_length=20)
	shares = forms.DecimalField(decimal_places=0, max_digits=40)
	isBuy = forms.BooleanField()
	buyingPrice = forms.DecimalField(decimal_places = 2, max_digits=40)

class LeagueForm(forms.Form):
	lname = forms.CharField(max_length=50)
	endDate = forms.CharField(max_length=20)
	startBalance = forms.DecimalField(decimal_places=2,max_digits=40)
	leagueType = forms.CharField(max_length=10)
	joinpwd = forms.CharField(max_length=20)
	#def clean_date(self):
	#	endDate = self.cleaned_data['endDate']
	#	if date < datetime.now():
	#		raise forms.ValidationError("The date cannot be in the past!")
	#	return endDate

class LoginForm(forms.Form):
	username = forms.CharField(label='Your name', max_length=20)
	password = forms.CharField(max_length=20)

