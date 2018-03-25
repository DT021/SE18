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
	playerID2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2')
	playerID3 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player3')
	playerID4 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player4')
	playerID5 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player5')
	playerID6 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player6')
	playerID7 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player7')
	playerID8 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player8')
	playerID9 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player9')
	playerID10 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player10')
	playerID11 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player11')
	playerID12 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player12')
	playerID13 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player13')
	playerID14 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player14')
	playerID15 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player15')
	playerID16 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player16')
	playerID17 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player17')
	playerID18 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player18')
	playerID19 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player19')
	playerID20 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player20')

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
