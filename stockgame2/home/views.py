from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from home.models import Player, League,Transaction, Asset
from django.contrib.auth.models import User as auth_User
from home.forms import SignUpForm, LeagueForm, BuyForm, JoinLeagueForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import datetime
import psycopg2
from django.contrib.auth import logout

def logout_view(request):
	logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect('/accounts/login')
def newLeague(request):
	date_inpast = False
	current_user = request.user
	if (request.method == 'POST' and current_user.is_authenticated):
		form = LeagueForm(request.POST)
		if form.is_valid():
			lname = form.cleaned_data.get('lname')
			joinpwd = form.cleaned_data.get('joinpwd')
			startbal = form.cleaned_data.get('startBalance')
			ltype = form.cleaned_data.get('leagueType')
			enddate = form.cleaned_data.get('endDate')
			date_out = datetime.datetime(*[int(v) for v in enddate.replace('T', '-').replace(':', '-').split('-')])
			
			b = False
			if ltype=="crypto":
				b = True
			new_league = League(adminID = current_user.id,name=lname,numPlayers=1,joinPassword=joinpwd,startingBalance=startbal,isCrypto=b, endDate=date_out,isUniversal=False)
			new_league.save()
			newPlayer = Player(leagueID=new_league,userID=current_user, buyingPower = startbal,percentChange=0,totalWorth=0)
			newPlayer.save()
			return HttpResponseRedirect('/dashboard')
		else:
			return render(request, 'createleague.html', {'form': form})
	else:
		form = SignUpForm()
		return render(request, 'createleague.html', {'form': form})
def joinLeague(request):
	current_user = request.user
	if request.method == 'POST':
		form = JoinLeagueForm(request.POST)
		if form.is_valid():
			password = form.cleaned_data.get('password')
			username = form.cleaned_data.get('username')
			league = League.objects.get(name=username)
			#print(league)
			# try:
				# password = form.cleaned_data.get('password')
				# username = form.cleaned_data.get('username')
				# league = League.objects.get(name=username)
			# except:
				# return HttpResponseRedirect('/joinLeague')
			if league.joinPassword == password:
				players = Player.objects.filter(leagueID = league)
				for p in players:
					if p.userID == current_user:
						return HttpResponseRedirect('/joinLeague')
				newPlayer = Player(leagueID=league,userID=current_user, buyingPower = league.startingBalance,percentChange=0,totalWorth=0)
				newPlayer.save()
			return HttpResponseRedirect('/dashboard')
		else:
			return render(request, 'joinleague.html', {'form': form})
	else:
		form = SignUpForm()
		return render(request, 'joinleague.html', {'form': form})
def submitSignup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			auth_login(request, user)
			return redirect('/home')
			# pwd = form.cleaned_data.get('password')
			# c_pwd = form.cleaned_data['conf_pwd']
			# if pwd!=c_pwd:
				# form.add_error('conf_pwd', "Password does not match")
				# return render(request, 'signup.html', {'form': form})
			# email = form.cleaned_data['email']
			# user = User(username=username, password=pwd, email=email, leagueID0 = 0, leagueID1 = 0, leagueID2 = 0, leagueID3 = 0)
			# user.save()
			# user = User.objects.create_user(username,pwd,email)
			# user.save()
			# return HttpResponseRedirect('/home')
		else:
			return render(request, 'signup.html', {'form': form})
	else:
		form = SignUpForm()
		return render(request, 'signup.html', {'form': form})

def submitBuy(request):
	if request.method == 'POST' and False:
		form = BuyForm(request.POST)
		if form.is_valid():
			current_user = request.user
			ticker = form.cleaned_data.get('ticker')
			shares = form.cleaned_data.get('shares')
			buyingPrice = form.cleaned_data.get('buyingPrice')
			new_asset = Asset(ticker = ticker, playerID = current_user.player, leagueID = "tmpLeagueID", shares = shares, buyingPrice = buyingPrice)
			new_asset.save()
			tmpPrice = 0
			new_transaction = Transaction(leagueID = "tmpLeagueID", playerID = current_user.playerID, price = tmpPrice, ticker = ticker, shares = share, isBuy = True)
			new_transaction.save()
			return redirect('/home')
			
		else:
			 #return redirect("/dashboard")
			return render(request, 'buypage.html', {'form': form})
	else:
		form = BuyForm()
		#return redirect("/dashboard")
		return render(request, 'buypage.html', {'form': form})

def submitSell(request):
	"""if request.method == 'POST':
		form = SellForm(request.POST)
		return redirect("/dashboard")
		if form.is_valid():
			form.save()
			ticker = form.cleaned_data.get('ticker')
			num_shares = form.cleaned_data.get('shares')
			user = authenticate(ticker=ticker, shares=num_shares)
			auth_login(request, user)
			return redirect('/home')
			# pwd = form.cleaned_data.get('password')
			# c_pwd = form.cleaned_data['conf_pwd']
			# if pwd!=c_pwd:
				# form.add_error('conf_pwd', "Password does not match")
				# return render(request, 'signup.html', {'form': form})
			# email = form.cleaned_data['email']
			# user = User(username=username, password=pwd, email=email, leagueID0 = 0, leagueID1 = 0, leagueID2 = 0, leagueID3 = 0)
			# user.save()
			# user = User.objects.create_user(username,pwd,email)
			# user.save()
			# return HttpResponseRedirect('/home')
		else:
			#return render(request, 'sellform.html', {'form': form})
			return redirect("/dashboard")
	else:"""
		#form = SellForm()
	return redirect("/dashboard")
		#return render(request, 'sellform.html', {'form': form})


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

	current_user = request.user
	if (current_user.is_authenticated):
		conn = psycopg2.connect(dbname="gyesfxht", user="gyesfxht", password="VwftaOkFDwF2LoGElDUxJ7i4kjJyALvy", host="stampy.db.elephantsql.com", port="5432")
		cur = conn.cursor()
		cur.execute('SELECT * from "home_player" WHERE "userID_id" = %s', [current_user.id])
		x = cur.fetchall()
		# context = {
		# 'league0': x[0],
		# 'league1': x[1]
		# }

		players = Player.objects.filter(userID=request.user)
		#print(players)
		return render(request, 'dashboard.html', {'players': players})
		# template = loader.get_template('dashboard.html')
		# return HttpResponse(template.render({},request))
	else:
		template = loader.get_template('anonuser.html')
		return HttpResponse(template.render({},request))

def createleague(request):
	date_inpast = False
	template = loader.get_template('createleague.html')
	return HttpResponse(template.render({},request))
def faq(request):
	template = loader.get_template('faq.html')
	return HttpResponse(template.render({},request))
def universal(request):
	template = loader.get_template('universalleague.html')
	return HttpResponse(template.render({},request))
def leagues(request,league_id):
	league = League.objects.get(pk=league_id)
	players = Player.objects.filter(leagueID = league)
	for p in players:
		if p.userID.id == league.adminID:
			admin = p.userID # admin is auth_user object
		if p.userID.id == request.user.id:
			currPlayer = p
	return render(request, 'individualleague.html', {'league': league, 'admin': admin, 'currPlayer':currPlayer})
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
	current_user = request.user
	if (current_user.is_authenticated):
		template = loader.get_template('profile.html')
		return HttpResponse(template.render({},request))
	else:
		template = loader.get_template('anonuser.html')
		return HttpResponse(template.render({},request))

def mission(request):
	template = loader.get_template('mission.html')
	return HttpResponse(template.render({},request))
def joinleague(request):
	template = loader.get_template('joinleague.html')
	return HttpResponse(template.render({},request))
def anonuser(request):
	template = loader.get_template('anonuser.html')
	return HttpResponse(template.render({},request))
def settings(request):
	template = loader.get_template('settings.html')
	return HttpResponse(template.render({},request))
# Create your views here.
