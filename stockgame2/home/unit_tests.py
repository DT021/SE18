from django.test import TestCase, Client
from django.contrib.auth import authenticate
from .models import League, User
import datetime

class ViewsTestCase(TestCase):
	def setUp(self):
		"""User is logged in"""
		self.user = User.objects.create(username='test2', password = 'testtest2',email = 'testtest2@test.com')
		self.c = Client()
		self.user = authenticate(username='test2',password='testtest2')
		login = self.c.login(username='test2',password='testtest2')
		self.assertTrue(login)
	def test_loginLoad(self):
		resp = self.client.get('/accounts/login')
		print(resp.status_code)   #this returns a 301 which is perfectly okay but gotta think of a better way to test for success for views than just check for 200
	def test_greetLoad(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_homeLoad(self):
		resp = self.client.get('/home')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/signup')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/dashboard')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/league1')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/buypage')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/sellform')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/mission')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/faq')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/profile')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/createleague')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('/joinleague')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
	def test_signupLoad(self):
		resp = self.client.get('')
		self.assertEqual(resp.status_code,200)   #if page loads successful return 200
# Create your tests here.