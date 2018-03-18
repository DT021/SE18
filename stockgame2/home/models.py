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


class Asset(models.Model):
		
