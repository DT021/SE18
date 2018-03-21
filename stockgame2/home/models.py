from django.db import models
# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=20)
        password = models.CharField(max_length=20)
        email = models.CharField(max_length=40)
        leagueID0 = models.IntegerField()
        leagueID1 = models.IntegerField()
        leagueID2 = models.IntegerField()
        leagueID3 = models.IntegerField()

class Setting(models.Model):
	beginDate = models.DateTimeField()
        endDate = models.DateTimeField()
        startingBalance = models.DecimalField(decimal_places=2,max_digits=25)
	adminID = models.IntegerField()
        isCrypto = models.BooleanField()
        joinPassword = models.CharField(max_length=20)
	
class Player(models.Model):
        userID = models.ForeignKey(
		User,
		on_delete=models.CASCADE
		verbose_name="the related user",
	)
        buyingPower = models.DecimalField(decimal_places=2,max_digits=25)
        percentChange = models.DecimalField(decimal_places=2,max_digits=25)
        totalWorth = models.DecimalField(decimal_places=2,max_digits=25)


class League(models.Model):


class Transaction(models.Model):
        leagueID = models.ForeignKey(
                League,
                on_delete=models.CASCADE
                verbose_name="the related league",
        )
	playerID = models.IntegerField()
	price = models.DecimalField(decimal_places=2,max_digits=25)
	ticker = models.CharField(max_length=5)
	shares = models.IntegerField()
	isBuy = models.BooleanField()

class Asset(models.Model):
	ticker = models.CharField(max_length=5)
	playerID = models.IntegerField()
	shares = models.IntegerField()
	buyingPrice = models.DecimalField(decimal_places=2,max_digits=25)
