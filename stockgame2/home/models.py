from django.db import models

# Create your models here.

class User(models.Model):
	userID = models.IntegerField()
	username = models.CharField(max_length=20)
        password = models.CharField(max_length=20)
        email = models.CharField(max_length=40)
        leagueID0 = models.IntegerField()
        leagueID1 = models.IntegerField()
        leagueID2 = models.IntegerField()
        leagueID3 = models.IntegerField()

class Setting(models.Model):

	
class Player(models.Model):


class League(models.Model):


class Transaction(models.Model):
	transactionID = models.IntegerField()
	leagueID = models.IntegerField()
	playerID = models.IntegerField()
	price = models.DecimalField(decimal_places=2,max_digits=10)
	ticker = models.CharField(max_length=5)
	amtShares = models.IntegerField()
	isBuy = models.BooleanField()

class Asset(models.Model):
	ticker = models.CharField(max_length=5)
	playerID = models.IntegerField()
	amtShares = models.IntegerField()
	buyingPrice = models.DecimalField(decimal_places=2,max_digits=10)