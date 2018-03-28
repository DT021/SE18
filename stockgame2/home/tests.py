from django.test import TestCase
from .models import League

class LeagueTestCase(TestCase):
	def setUp(self):
		League.objects.create(name="testLeague", isUniversal=False,numPlayers=15,beginDate=datetime.now,endDate = datetime.now()+datetime.timedelta(days=1),startingBalance = 25.36,adminID = 3, isCrypto = True, joinPassword = "pwd")

	def test_LeagueCreated(self):
		"""Leagues are correctly identified"""
		league1 = League.objects.get(name="testLeague")
		self.assertEqual(league1.isUniversal, False)
# Create your tests here.
