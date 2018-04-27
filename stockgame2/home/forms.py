from django import forms
from django.shortcuts import render
import datetime
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as auth_User
from home.models import Player, League, Asset
from home.financepi import getPriceFromAPI

class SignUpForm(UserCreationForm):
	class Meta:
		model = auth_User
		fields = ('username', 'password1', 'password2', 'email')

class BuyForm(forms.Form):
	ticker = forms.CharField(max_length=20)
	shares = forms.DecimalField(decimal_places=0, max_digits=40)
	isCrypto = forms.BooleanField(required = False)
	buyingPrice = forms.DecimalField(decimal_places = 2, max_digits=40, required=False)
	def clean_ticker(self):
		isCrypto = False
		ticker = self.cleaned_data['ticker']
		buyingPrice = getPriceFromAPI(ticker,isCrypto)
		if buyingPrice == -1:
			raise ValidationError(_("Ticker does not exist. "))
		elif buyingPrice == -22:
			raise ValidationError(_("Too many requests at this time."))
		elif buyingPrice <0:
			raise ValidationError (_("Invalid input"))
		return ticker
	

class SellForm(forms.Form):
	#ticker = forms.CharField(max_length=20)
	shares = forms.DecimalField(decimal_places=0, max_digits=40)
	selltype = forms.CharField(max_length=20, required=False)
	limitPrice = forms.DecimalField(decimal_places = 2, max_digits=40, required=False)
	stopPrice = forms.DecimalField(decimal_places = 2, max_digits=40, required=False)
	
class CreateAiForm(forms.Form):
	ainame = forms.CharField(max_length=50)
	leaguename = forms.CharField(max_length=50)
		
class LeagueForm(forms.Form):
	lname = forms.CharField(max_length=50)
	endDate = forms.CharField(max_length=20)
	startBalance = forms.DecimalField(decimal_places=2,max_digits=40)
	leagueType = forms.CharField(max_length=10)
	joinpwd = forms.CharField(max_length=20)
	def clean_endDate(self):
		enddate = self.cleaned_data['endDate']
		date_out = datetime.datetime(*[int(v) for v in enddate.replace('T', '-').replace(':', '-').split('-')])
		if date_out < datetime.datetime.now():
			raise ValidationError(_("The date cannot be in the past!"))
			date_inpast = True
			#return render(request, 'createleague.html', {'form': form})
		return enddate

class JoinLeagueForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=20)
	def clean_username(self):
		try:
			password = self.cleaned_data.get('password')
			username = self.cleaned_data.get('username')
			league = League.objects.get(name=username)
			
		except:
			raise ValidationError(_("League does not exist!"))
		
		return username
	def clean_password(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		try:
			league = League.objects.get(name=username)
		except:
			raise ValidationError(_("League does not exist!"))
		if league.joinPassword == password:
			return password
		else:
			raise ValidationError(_("Password is incorrect!"))
		return password	

class LoginForm(forms.Form):
	username = forms.CharField(label='Your name', max_length=20)
	password = forms.CharField(max_length=20)
