from django.db import models
from django.conf import settings
from datetime import datetime  
from django.contrib.auth.models import User as auth_User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(auth_User, on_delete=models.CASCADE)
	trophies = ArrayField(models.IntegerField(), size = 8)
	statement = models.CharField(max_length=250)
	name = models.CharField(max_length=40)
	birthday = models.DateTimeField()
	
class League(models.Model):
	name = models.CharField(max_length=50)
	isUniversal = models.BooleanField()
	numPlayers = models.IntegerField()
	beginDate = models.DateTimeField(default=datetime.now, blank=True)
	endDate = models.DateTimeField()
	startingBalance = models.DecimalField(decimal_places=2,max_digits=40)
	adminID = models.IntegerField()
	isCrypto = models.BooleanField()
	joinPassword = models.CharField(max_length=20)
	
class Player(models.Model):
	leagueID = models.ForeignKey(League, on_delete=models.CASCADE)
	userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	buyingPower = models.DecimalField(decimal_places=2,max_digits=25)
	percentChange = models.DecimalField(decimal_places=2,max_digits=25)
	totalWorth = models.DecimalField(decimal_places=2,max_digits=25)


class Transaction(models.Model):
	leagueID = models.ForeignKey(League, on_delete=models.CASCADE)
	playerID = models.IntegerField()
	price = models.DecimalField(decimal_places=2,max_digits=25)
	ticker = models.CharField(max_length=5)
	shares = models.IntegerField()
	isBuy = models.BooleanField()

class Asset(models.Model):
	ticker = models.CharField(max_length=5)
	playerID = models.IntegerField()
	leagueID = models.ForeignKey(League, on_delete=models.CASCADE)
	shares = models.IntegerField()
	buyingPrice = models.DecimalField(decimal_places=2,max_digits=25)
