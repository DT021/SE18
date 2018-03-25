from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('get_user', views.get_user, name = 'get_user'),
	path('submitSignup', views.submitSignup, name = 'submitSignup'),
	path('signup', views.signup, name ='signup'),
	path('login', views.login, name='login'),
        path('submitLogin', views.submitLogin, name = 'submitLogin'),
	path('aboutus', views.aboutus, name='aboutus'),
	path('home', views.home, name='home'),
	path('dashboard', views.dashboard, name='dashboard'),
	path('createleague', views.createleague, name='createleague'),
	path('universal', views.universal, name='universal'),
	path('league1', views.league1, name='league1'),
	path('league2', views.league2, name='league2'),
	path('league3', views.league3, name='league3'),
	path('profile', views.profile, name='profile'),
	path('faq', views.faq, name='faq'),
	path('buypage', views.buypage, name='buypage'),
	path('sellform', views.sellform, name='sellform'),
	path('profile', views.profile, name='profile'),
	path('mission', views.mission, name="mission")
	]
