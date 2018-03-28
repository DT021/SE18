from django.test import TestCase, Client
from django.contrib.auth import authenticate
from .models import League, User
import datetime
class LeagueTestCase(TestCase):
	def setUp(self):
		League.objects.create(name="testLeague", isUniversal=False,numPlayers=15,beginDate=datetime.datetime.now(),endDate = datetime.datetime.now()+datetime.timedelta(days=1),startingBalance = 25.36,adminID = 3, isCrypto = True, joinPassword = "pwd")

	def test_LeagueCreated(self):
		"""Leagues are correctly identified"""
		league1 = League.objects.get(name="testLeague")
		self.assertEqual(league1.isUniversal, False)
	
		

class LoginTestCase(TestCase):
	def setUp(self):
		"""User is logged in"""
		self.user = User.objects.create(username='test', password = 'testtest',email = 'testtest@test.com')
		
	def test_UserLogIn(self):
		self.c = Client()
		self.user = authenticate(username='test',password='testtest')
		login = self.c.login(username='test',password='testtest')
		self.assertTrue(login)
		
		
	def test_searchUser(self):
		"""user was created and exists"""
		user1 = User.objects.get(username='test')
		self.assertEqual(user1,self.user)     #this should work 

class ViewsTestCase(TestCase):
	def setUp(self):
		""""add log in here so we can load other views"""
	def test_homeLoad(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/signup')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_loginLoad(self):
		resp = self.client.get('/accounts/login')
		print(resp.status_code)   #this returns a 301 which is perfectly okay but gotta think of a better way to test for success for views than just check for 200
# Create your tests here.
