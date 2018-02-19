from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('signup', views.signup, name ='signup'),
	path('aboutus', views.aboutus, name='aboutus'),
	]