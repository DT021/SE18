from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.core import validators

class UserForm(forms.Form):
	username = forms.CharField(label='Your name', max_length=20)
	password = forms.CharField(max_length=20)
	conf_pwd = forms.CharField(max_length=20)
	email = forms.CharField(max_length=40, validators=[validators.validate_email])

class LeagueForm(forms.Form):
	isUniversal = forms.BooleanField()
	numPlayers = forms.IntegerField()
	beginDate = forms.DateTimeField()
	endDate = forms.DateTimeField()
	startingBalance = forms.DecimalField(decimal_places=2,max_digits=40)
	adminID = forms.IntegerField()
	isCrypto = forms.BooleanField()
	joinPassword = forms.CharField(max_length=20)