from django.db import models
from django.conf import settings
from datetime import datetime  
from django.contrib.auth.models import User as auth_User
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError


# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(auth_User, on_delete=models.CASCADE)
	trophies = ArrayField(models.IntegerField(default = 0), size = 8,default=[0]*8)
	statement = models.CharField(max_length=250, default = '')
	name = models.CharField(max_length=40, default='')
	birthday = models.DateTimeField(null=True)
	TitanCoins = models.IntegerField(default = 0)

@receiver(post_save, sender=auth_User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=auth_User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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
	hasEnded = models.BooleanField()
	
class Player(models.Model):
	leagueID = models.ForeignKey(League, on_delete=models.CASCADE)
	userID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	buyingPower = models.DecimalField(decimal_places=2,max_digits=25)
	percentChange = models.DecimalField(decimal_places=2,max_digits=25)
	totalWorth = models.DecimalField(decimal_places=2,max_digits=25)
	isAi = models.BooleanField(False)
	cumWorth = models.DecimalField(decimal_places=2,max_digits=35)


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
