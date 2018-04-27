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
	isCrypto = forms.BooleanField()
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
	# def clean_shares(self):
		# isCrypto = False
		# ticker = self.cleaned_data['ticker']
		# shares = self.cleaned_data['shares']
		# buyingPrice = getPriceFromAPI(ticker,isCrypto)
		# tmpPrice = buyingPrice*shares
		# if tmpPrice > player.buyingPower:
			# raise ValidationError (_("Current balance insufficient."))
		# return shares

class SellForm(forms.Form):
	#ticker = forms.CharField(max_length=20)
	shares = forms.DecimalField(decimal_places=0, max_digits=40)
	selltype = forms.CharField(max_length=20, required=False)
	limitPrice = forms.DecimalField(decimal_places = 2, max_digits=40, required=False)
	stopPrice = forms.DecimalField(decimal_places = 2, max_digits=40, required=False)
	# def clean(self):
		# asset = Asset.objects.get(pk=asset_id)
		# if shares > asset.shares:
			# raise ValidationError(_("You do not own this many shares."))
			# return render(request, 'sellform.html', {'form': form})
	
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
