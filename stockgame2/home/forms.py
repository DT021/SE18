from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as auth_User

class SignUpForm(UserCreationForm):
	# username = forms.CharField(label='Your name', max_length=20)
	# password = forms.CharField(max_length=20)
	# conf_pwd = forms.CharField(max_length=20)
	email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
	class Meta:
		model = auth_User
		fields = ('username', 'password1', 'password2', 'email')
class signupform2(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)
	email = forms.CharField(max_length=50)
class LeagueForm(forms.Form):
	isUniversal = forms.BooleanField()
	numPlayers = forms.IntegerField()
	beginDate = forms.DateTimeField()
	endDate = forms.DateTimeField()
	startingBalance = forms.DecimalField(decimal_places=2,max_digits=40)
	isCrypto = forms.BooleanField()
	joinPassword = forms.CharField(max_length=20)

class LoginForm(forms.Form):
	username = forms.CharField(label='Your name', max_length=20)
	password = forms.CharField(max_length=20)

