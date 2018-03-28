from django.test import TestCase, Client
from .models import League

class LeagueTestCase(TestCase):
	def setUp(self):
		League.objects.create(name="testLeague", isUniversal=False,numPlayers=15,beginDate=datetime.now,endDate = datetime.now()+datetime.timedelta(days=1),startingBalance = 25.36,adminID = 3, isCrypto = True, joinPassword = "pwd")

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
		
# Create your tests here.
