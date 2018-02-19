from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render({},request))
def signup(request):
	template = loader.get_template('signup.html')
	return HttpResponse(template.render({},request))
def aboutus(request):
	template = loader.get_template('aboutus.html')
	return HttpResponse(template.render({},request))
# Create your views here.
