from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from home.models import User
from home.forms import UserForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.validators import validate_email


def submitSignup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			pwd = form.cleaned_data['password']
			c_pwd = form.cleaned_data['conf_pwd']
			if pwd!=c_pwd:
				form.add_error('conf_pwd', "Password does not match")
				return render(request, 'signup.html', {'form': form})
			email = form.cleaned_data['email']
			user = User(username=username, password=pwd, email=email, leagueID0 = 0, leagueID1 = 0, leagueID2 = 0, leagueID3 = 0)
			user.save()
			return HttpResponseRedirect('/home')
		else:
			return render(request, 'signup.html', {'form': form})
	else:
		form = UserForm()

		return render(request, 'signup.html', {'form': form})
#    savedUser = request.POST.get("username", "")
#    savedPass = request.POST.get("password1", "")
#    confirmPass = request.POST.get("password2", "")
#    if password != confirmPass: # redirect to signup with error message
#        template = loader.get_template('signup.html')
   #     return HttpResponse(template.render({},request))
 #   savedEmail = request.POST.get("email", "")
#    user = User(username=savedUser, password=savedPass, email=savedEmail, leagueID0 = 0, leagueID1 = 0, leagueID2 = 0, leagueID3 = 0)
#    user.save()
# # user2 = User(username="savedUser", password="savedPass", email="savedEmail", leagueID0 = 0, leagueID1 = 0, leagueID2 = 0, leagueID3 = 0)
# # user2.save()
 #   template = loader.get_template('aboutus.html') # should redirect to profile page with message indicating successful profile creation
#    return HttpResponse(template.render({},request))
# # template = loader.get_template('aboutus.html')
# # return HttpResponse(template.render({},request))
	
def get_user(request):
	 # if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = UserForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			form.save()
			return HttpResponseRedirect('/aboutus')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = UserForm()

	return render(request, 'user.html', {'form': form})

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
	template = loader.get_template('universalleague.html')
	return HttpResponse(template.render({},request))
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
