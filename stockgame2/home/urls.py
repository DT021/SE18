from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('signup', views.signup, name ='signup'),
	path('aboutus', views.aboutus, name='aboutus'),
	path('home', views.home, name='home'),
	path('dashboard', views.dashboard, name='home'),
	path('createleague', views.createleague, name='home'),
	path('universal', views.universal, name='universal'),
	path('league1', views.league1, name='league1'),
	path('league2', views.league2, name='league2'),
	path('league3', views.league3, name='league3'),
	path('profile', views.profile, name='profile')
	]