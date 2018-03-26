from django.db import models
from datetime import datetime  

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
	beginDate = models.DateTimeField(default=datetime.now, blank=True)
	endDate = models.DateTimeField()
	startingBalance = models.DecimalField(decimal_places=2,max_digits=40)
	adminID = models.IntegerField()
	isCrypto = models.BooleanField()
	joinPassword = models.CharField(max_length=20)

class Player(models.Model):
	userID = models.ForeignKey(User, on_delete=models.CASCADE)
	buyingPower = models.DecimalField(decimal_places=2,max_digits=25)
	percentChange = models.DecimalField(decimal_places=2,max_digits=25)
	totalWorth = models.DecimalField(decimal_places=2,max_digits=25)

class League(models.Model):
	name = models.CharField(max_length=50)
	isUniversal = models.BooleanField()
	settingID = models.ForeignKey(Setting, on_delete=models.CASCADE)
	numPlayers = models.IntegerField()
	playerID1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1')
	playerID2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2', blank=True)
	playerID3 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player3', blank=True)
	playerID4 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player4', blank=True)
	playerID5 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player5', blank=True)
	playerID6 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player6', blank=True)
	playerID7 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player7', blank=True)
	playerID8 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player8', blank=True)
	playerID9 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player9', blank=True)
	playerID10 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player10', blank=True)
	playerID11 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player11', blank=True)
	playerID12 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player12', blank=True)
	playerID13 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player13', blank=True)
	playerID14 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player14', blank=True)
	playerID15 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player15', blank=True)
	playerID16 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player16', blank=True)
	playerID17 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player17', blank=True)
	playerID18 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player18', blank=True)
	playerID19 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player19', blank=True)
	playerID20 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player20', blank=True)

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
