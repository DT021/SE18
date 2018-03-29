from django.test import TestCase, Client
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import League, Player,Transaction,Asset
from django.utils import timezone
import datetime
class IntegerTestCase(TestCase):
	def setUp(self):
		self.league = League.objects.create(name="testLeague", isUniversal=False,numPlayers=15,beginDate=timezone.now(),endDate = timezone.now()+datetime.timedelta(days=1),startingBalance = 25.36,adminID = 3, isCrypto = True, joinPassword = "pwd")
		self.user = User.objects.create_user(username='test', password = 'testtest',email = 'testtest@test.com')
		self.c = Client()
		self.player = Player.objects.create(leagueID=self.league,userID=self.user,buyingPower=10.0,percentChange=10.0,totalWorth=10.0)
		self.transaction = Transaction.objects.create(leagueID=self.league,playerID=1,price=5.5,ticker="GOOG",shares=1,isBuy=True) #check if player id is supposed to be int or obj
		self.asset = Asset.objects.create(ticker="GOOG", playerID = 1, leagueID=self.league,shares=1,buyingPrice=5.5)
		
	def test_LeagueCreated(self):
		league1 = League.objects.get(name="testLeague")
		self.assertEqual(league1.isUniversal, False)
		
	def test_UserLogIn(self):
		"""User is logged in"""
		self.user = authenticate(username='test',password='testtest')
		login = self.c.login(username='test',password='testtest')
		self.assertTrue(login)
		print("User is logged in")
		
	def test_UserLogOut(self):
		self.user = authenticate(username='test',password='testtest')
		login = self.c.login(username='test',password='testtest')
		self.assertTrue(login)
		
		logout = self.c.logout()
		print("User has logged out")
	
	def test_PlayerCreated(self):
		player2 = Player.objects.get(leagueID=self.league, userID=self.user)
		print("Player has been found")
		self.assertEqual(self.player, player2)
		
	def test_UserCreated(self):
		
		user1 = User.objects.get(username='test')
		self.assertEqual(user1,self.user)  
		print("User was created and exists")
		
	def test_TransactionCreated(self):
		t1 = Transaction.objects.get(playerID=1,leagueID=self.league)
		self.assertEqual(t1,self.transaction)
		print("Transaction created")
		
	def test_updateBuyBP(self):
		self.player.buyingPower = self.player.buyingPower + self.transaction.price
		t1 = Transaction.objects.get(playerID=1,leagueID=self.league)
		player2 = Player.objects.get(leagueID=self.league, userID=self.user)
		test = player2.buyingPower + t1.price
		self.assertTrue(test>=0)
		print("Transaction is valid")
		
		self.assertTrue(self.player.buyingPower,player2.buyingPower)
		print("Buying Power Updated")
		
	def test_AssetCreated(self):
		asset1 = Asset.objects.get(ticker="GOOG", playerID = 1)
		self.assertEqual(asset1, self.asset)
	

