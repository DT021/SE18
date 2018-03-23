from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from home.models import User

def submitSignup(request):
#    savedUser = request.POST.get("username", "")
#    savedPass = request.POST.get("password1", "")
#    confirmPass = request.POST.get("password2", "")
#    if password != confirmPass: # redirect to signup with error message
#        template = loader.get_template('signup.html')
   #     return HttpResponse(template.render({},request))
 #   savedEmail = request.POST.get("email", "")
#    user = User(username=savedUser, password=savedPass, email=savedEmail, leagueID0 = 0, leagueID1 = 0, leagueID2 = 0, leagueID3 = 0)
#    user.save()
    user2 = User(username="savedUser", password="savedPass", email="savedEmail", leagueID0 = 0, leagueID1 = 0, leagueID2 = 0, leagueID3 = 0)
    user2.save()
 #   template = loader.get_template('aboutus.html') # should redirect to profile page with message indicating successful profile creation
#    return HttpResponse(template.render({},request))
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render({},request))

def index(request):
	template = loader.get_template('greet.html')
	return HttpResponse(template.render({},request))
def signup(request):
	template = loader.get_template('signup.html')
	return HttpResponse(template.render({},request))
def login(request):
	template = loader.get_template('login.html')
	return HttpResponse(template.render({},request))
def aboutus(request):
	template = loader.get_template('aboutus.html')
	return HttpResponse(template.render({},request))
def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render({},request))
def dashboard(request):
	template = loader.get_template('dashboard.html')
	return HttpResponse(template.render({},request))
def createleague(request):
	template = loader.get_template('createleague.html')
	return HttpResponse(template.render({},request))
def faq(request):
	template = loader.get_template('faq.html')
	return HttpResponse(template.render({},request))
def universal(request):
	return HttpResponse("This is the universal league page.")
def league1(request):	# (request, league_id)
	template = loader.get_template('individualleague.html')
	return HttpResponse(template.render({},request))
def league2(request):
	return HttpResponse("This is the league2 page.")
def league3(request):
	return HttpResponse("This is the league3 page.")
def buypage(request):
	template = loader.get_template('buypage.html')
	return HttpResponse(template.render({},request))
def sellform(request):
	template = loader.get_template('sellform.html')
	return HttpResponse(template.render({},request))
def profile(request):
	template = loader.get_template('profile.html')
	return HttpResponse(template.render({},request))
def mission(request):
	template = loader.get_template('mission.html')
	return HttpResponse(template.render({},request))
# Create your views here.
