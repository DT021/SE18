from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core import validators
from home.models import Player, League,Transaction, Asset, Profile
from django.contrib.auth.models import User as auth_User
from home.forms import SignUpForm, LeagueForm, BuyForm, JoinLeagueForm, SellForm, CreateAiForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import datetime
from django.utils import timezone
import psycopg2
from django.contrib.auth import logout
from home.financepi import getPriceFromAPI
import decimal
from django.contrib.postgres.fields import ArrayField
from django.views.decorators.csrf import csrf_exempt
# from home.easyai import *
# from home.medai import *
# from home.hardai import *

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
			newPlayer = Player(leagueID=new_league,userID=current_user, buyingPower = startbal,percentChange=0,totalWorth=0, cumWorth = startbal)
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
			#if league.joinPassword == password:
			# #league.numPlayers = 0
			# # for p in players:
				# # league.numPlayers+=1
			players = Player.objects.filter(leagueID = league)
			for p in players:
				if p.userID == current_user:
					return HttpResponseRedirect('/joinLeague')
			
			newPlayer = Player(leagueID=league,userID=current_user, buyingPower = league.startingBalance,percentChange=0,totalWorth=0,isAi=False, cumWorth = league.startingBalance)
			league.numPlayers+=1
			league.save()
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
			# pr = Profile()
			# pr.trophies[0] = 0
			# pr.trophies[1] = 0
			# pr.trophies[2] = 0
			# pr.trophies[3] = 0
			# pr.trophies[4] = 0
			# pr.trophies[5] = 0
			# pr.trophies[6] = 0
			# pr.trophies[7] = 0
			# pr.statement = ''
			# pr.name = ''
			# pr.TitanCoins = 0
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			user.save()
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
			print('invalid')
			return render(request, 'signup.html', {'form': form})
	else:
		form = SignUpForm(request.POST)
		return render(request, 'signup.html', {'form': form})

def submitBuy(request,league_id,player_id):
	league = League.objects.get(pk=league_id)
	player = Player.objects.get(pk=player_id)
	form = BuyForm(request.POST)

	if True:	
		form.is_valid()
		current_user = request.user
		ticker = form.cleaned_data.get('ticker')
	# if(ticker == 'GOOG'):
		# return redirect('/processInvalid')
	# else:
		shares = form.cleaned_data.get('shares')
		#isCrypto = form.cleaned_data.get('isCrypto')
		isCrypto = False
		#buyingPrice = form.cleaned_data.get('buyingPrice')
		buyingPrice = getPriceFromAPI(ticker,isCrypto) #allow crypto in future
		#player = Player.objects.get(id=3)
		#tempPid = 1
		#tempLid = League.objects.get(name="k1")
		tmpPrice = buyingPrice*shares
		if tmpPrice > player.buyingPower:
			storage = messages.get_messages(request)
			messages.add_message(request, messages.ERROR, 'You do not have sufficient balance.')
			storage.used = False
			return render(request, 'buypage.html', {'form': form,'league':league,'player':player})
		pAssets = Asset.objects.filter(leagueID = league,playerID = player.id)
		assetExists = False
		for i in pAssets:
			if i.ticker == ticker:
				assetExists = True
				new_asset = i
		if assetExists == False:
			new_asset = Asset(ticker = ticker, playerID = player.id, leagueID = league, shares = shares, buyingPrice = buyingPrice)
		else:
			new_asset.shares += shares
			new_asset.buyingPrice = buyingPrice
		new_asset.save()
		player.totalWorth += tmpPrice
		new_transaction = Transaction(leagueID = league, playerID = player.id, price = tmpPrice, ticker = ticker, shares = shares, isBuy = True)
		player.buyingPower -= tmpPrice
		player.cumWorth = player.totalWorth + player.buyingPower
		player.save()
		new_transaction.save()
		# update trophies array to count buys
		current_user.profile.trophies[0] += 1
		current_user.save()

		url = '/receipt/'+str(new_transaction.id)+'/'
		return redirect(url)
	else:
		return render(request, 'buypage.html', {'form': form,'league':league,'player':player})


def transactionReceipt(request,transaction_id):
	#lastTransaction = Transaction.objects.latest()
	lastTransaction = Transaction.objects.get(pk=transaction_id)
	#leagueID = lastTransaction.leagueID
	#playerID = lastTransaction.playerID
	price = lastTransaction.price
	ticker = lastTransaction.ticker
	shares = lastTransaction.shares
	return render(request, 'receipt.html', {'price': price, 'ticker': ticker, 'shares': shares})


def createai(request):
	form = CreateAiForm(request.POST)
	if(form.is_valid()):
		ainame = form.cleaned_data.get('ainame')
		leaguename = form.cleaned_data.get('leaguename')
		league = League.objects.get(name=leaguename)
		userid = auth_User.objects.filter(username = ainame)
		print(userid)
		newPlayer = Player(leagueID=league,userID=userid.first(), buyingPower = league.startingBalance,percentChange=0,totalWorth=0,isAi=True)
		league.numPlayers+=1
		league.save()
		newPlayer.save()
		return render(request, 'individualleague.html')
	else:
		return render(request, 'home.html')
# MUST UPDATE PLAYER BUYING POWER
def submitSell(request,league_id,player_id,asset_id):
	current_user = request.user
	if request.method == 'POST':
		form = SellForm(request.POST)
		if (form.is_valid() and current_user.is_authenticated):
			shares = form.cleaned_data.get('shares')
			player = Player.objects.get(pk=player_id)
			league = League.objects.get(pk=league_id)
			asset = Asset.objects.get(pk=asset_id)
			currShares = asset.shares
			if shares > currShares:
				storage = messages.get_messages(request)
				messages.add_message(request, messages.ERROR, 'You do not own this many shares.')
				storage.used = False
				return render(request, 'sellform.html', {'form': form, 'league':league,'player':player,'asset':asset})
			marketPrice = getPriceFromAPI(asset.ticker, False)
			sellTotal = marketPrice*shares
			player.buyingPower += sellTotal
			player.totalWorth -= sellTotal
			player.cumWorth = player.buyingPower + player.totalWorth
			player.save()
			# update trophies array to count sells
			current_user.profile.trophies[1] +=1
			current_user.save()
			asset.shares = currShares - shares
			if asset.shares == 0:
				asset.delete()
			else:
				asset.save()
			url = '/leagues/'+str(league.id)+'/'
			return redirect(url)
			

		else:

			return render(request, 'sellform.html', {'form': form})
	else:
		return render(request, 'buypage.html')


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

def sendinvite(request):
	current_user = request.user
	if(request.method == 'POST'):
		if(current_user.is_authenticated):
			#Make query for the league password
			conn = psycopg2.connect(dbname="gyesfxht", user="gyesfxht", password="VwftaOkFDwF2LoGElDUxJ7i4kjJyALvy", host="stampy.db.elephantsql.com", port="5432")
			cur = conn.cursor()
			cur.execute()

			x = cur.fetchone()

			#username = 
			league = League.objects.get(name=username)
			password = league.joinPassword
			send_mail(
				'Titan Trading League Invitation',
				'You have been invited to compete against your friends on Titan Trading, the leading fantasy stock trading application!\n To join just sign up for an account and press the \'Join League\' button on the dashboard. The league password is: ' + password + '\nWe look forward to seeing you join in on the fun!\nMay the odds be in your favor,\nThe Titan Trading Team'
				'titantrading@gmail.com',
				['to@example.com'],
				fail_silently=False,
			)


def index(request):
	template = loader.get_template('greet.html')
	return HttpResponse(template.render({},request))
def signup(request):
	template = loader.get_template('signup.html')
	return HttpResponse(template.render({},request))
def createaipage(request):
	template = loader.get_template('createaipage.html')
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
def buydash(ticker, shares, league_id, player_id):
	league = League.objects.get(pk=league_id)
	player = Player.objects.get(pk=player_id)
	buyingPrice = getPriceFromAPI(ticker,False)
	tmpPrice = buyingPrice*shares
	if tmpPrice > player.buyingPower:
		storage = messages.get_messages(request)
		messages.add_message(request, messages.ERROR, 'You do not have sufficient balance.')
		storage.used = False
		return render(request, 'dashboard.html')
	pAssets = Asset.objects.filter(leagueID = league,playerID = player.id)
	assetExists = False
	for i in pAssets:
		if i.ticker == ticker:
			assetExists = True
			new_asset = i
	if assetExists == False:
		new_asset = Asset(ticker = ticker, playerID = player.id, leagueID = league, shares = shares, buyingPrice = buyingPrice)
	else:
		new_asset.shares += shares
		new_asset.buyingPrice = buyingPrice
	new_asset.save()
	player.totalWorth += tmpPrice
	new_transaction = Transaction(leagueID = league, playerID = player.id, price = tmpPrice, ticker = ticker, shares = shares, isBuy = True)
	player.buyingPower -= tmpPrice
	player.cumWorth = player.totalWorth + player.buyingPower
	player.save()
	new_transaction.save()
def selldash(shares,player_id, league_id, asset_id):
	player = Player.objects.get(pk=player_id)
	league = League.objects.get(pk=league_id)
	asset = Asset.objects.get(pk=asset_id)
	currShares = asset.shares
	if shares > currShares:
		storage = messages.get_messages(request)
		messages.add_message(request, messages.ERROR, 'You do not own this many shares.')
		storage.used = False
		#raise forms.ValidationError("You do not own this many shares.")
		return render(request, 'sellform.html', {'form': form, 'league':league,'player':player,'asset':asset})
	marketPrice = getPriceFromAPI(asset.ticker, False)
	sellTotal = marketPrice*shares
	player.buyingPower += sellTotal
	player.totalWorth -= sellTotal
	player.cumWorth = player.buyingPower + player.totalWorth
	player.save()
	asset.shares = currShares - shares
	if asset.shares == 0:
		asset.delete()
	else:
		asset.save()
def dashboard(request):
	current_user = request.user
	if (current_user.is_authenticated):
		players = Player.objects.filter(userID=request.user)
		
		i = 1
		admin = list()
		rank = list()
		for p in players:

			count = 0

			currasset = list()
			curramt = list()
			result = list()
			people = Player.objects.filter(leagueID = p.leagueID).order_by('-cumWorth')
			assething = Asset.objects.filter(leagueID = p.leagueID)
			for l in people:
				if l.userID.id == 14:
					for h in assething:
						if h.playerID == l.id:
							currasset.append(h.ticker)
							curramt.append(h.shares)
					result = easyAI(p.leagueID.isCrypto,l.buyingPower,currasset,curramt)
					 #allow crypto in future
					shares = result[1]
					ticker = result[0]
					if shares != 0:
						buydash(ticker, shares,l.leagueID.id, l.id)
					print(result[3])
					print(currasset)
					print(curramt)
					if result[3] != 0:
						asset123 = Asset.objects.filter(ticker = result[2])
						print(result[2])
						print(asset123)
						selldash(result[3],l.id,l.leagueID.id,asset123.first().id)
					result.clear()
					currasset.clear()
					curramt.clear()
					
				if l.userID.id == 15:
					for h in assething:
						if h.playerID == l.id:
							currasset.append(h.ticker)
							curramt.append(h.shares)
					result = getBuy_med(l.buyingPower)
					ticker = result[0]
					shares = result[1]
					if shares != 0:
						buydash(ticker, shares,l.leagueID.id, l.id)
					print(currasset)
					print(curramt)
					result.clear()
					result = getSell_med(currasset,curramt)
					ticker = result[0]
					shares = result[1]
					if shares != 0:
						asset123 = Asset.objects.filter(ticker = ticker)
						print(asset123)
						selldash(shares,l.id,l.leagueID.id,asset123.first().id)
					result.clear()
					currasset.clear()
					curramt.clear()
				if l.userID.id == 16:
					for h in assething:
						if h.playerID == l.id:
							currasset.append(h.ticker)
							curramt.append(h.shares)
					result = getBuy_hard(l.buyingPower)
					ticker = result[0]
					shares = result[1]
					if shares != 0:
						buydash(ticker, shares,l.leagueID.id, l.id)
					print(currasset)
					print(curramt)
					result.clear()
					result = getSell_hard(currasset,curramt)
					ticker = result[0]
					shares = result[1]
					if shares != 0:
						asset123 = Asset.objects.filter(ticker = ticker)
						print(asset123)
						selldash(shares,l.id,l.leagueID.id,asset123.first().id)
					result.clear()
					currasset.clear()
					curramt.clear()


			for l in people:
				count+=1
				if l.userID.id == p.leagueID.adminID:
					admin.append(l.userID.username)
				if l.userID.id == request.user.id:
					rank.append(count)
			i = i + 1
			
			
		return render(request, 'dashboard.html', {'players': players, 'admin':admin,'rank':rank})

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
	current_user = request.user
	league = League.objects.get(pk=league_id)
	endDate = league.endDate
	presentDate = timezone.now()
	players = Player.objects.filter(leagueID = league).order_by('-cumWorth')
	count = 0 
	rank = 0
	numAIbeat = 0
	for p in players:
		count+=1
		if p.userID.id == league.adminID:
			admin = p.userID # admin is auth_user object
		if p.userID.id == request.user.id:
			currPlayer = p
			rank = count
		if p.isAi and count > 0: # AI placing worse than user
			numAIbeat += 1
	if (endDate < presentDate): # league has ended, redirect to leaderboard.html
		if not (league.hasEnded): # need to handle trophies
			league.hasEnded = True
			current_user.profile.trophies[3] += 1 # increment for game played
			if rank < 4: # top 3 = win
				current_user.profile.trophies[2] += 1 # increment for win
			current_user.profile.trophies[4] = current_user.profile.trophies[4] + numAIbeat 
			if admin.id == request.user.id: # this user is admin
				if current_user.profile.trophies[5] < count: # new record for # ppl managed
					current_user.profile.trophies[5] = count
			current_user.save()
		return render(request, 'leaderboard.html', {'league': league, 'admin': admin, 'players':players,'currPlayer':currPlayer, 'rank':rank})

	pAssets = Asset.objects.filter(playerID = currPlayer.id)
	print(pAssets)
	#players.order_by('-totalWorth')
	return render(request, 'individualleague.html', {'league': league, 'admin': admin, 'players':players,'currPlayer':currPlayer,'pAssets':pAssets,'rank':rank})

def league1(request):	# (request, league_id)
	template = loader.get_template('individualleague.html')
	return HttpResponse(template.render({},request))
def league2(request):
	return HttpResponse("This is the league2 page.")
def league3(request):
	return HttpResponse("This is the league3 page.")
def buypage(request,league_id,player_id):
	league = League.objects.get(pk=league_id)
	player = Player.objects.get(pk=player_id)
	return render(request, 'buypage.html', {'league': league,'player':player})
def sellform(request,league_id,player_id,asset_id):
	league = League.objects.get(pk=league_id)
	player = Player.objects.get(pk=player_id)
	asset = Asset.objects.get(pk=asset_id)
	return render(request, 'sellform.html', {'league': league,'player':player,'asset':asset})
def profile(request):
	current_user = request.user
	if (current_user.is_authenticated):
		template = loader.get_template('profile.html')
		return HttpResponse(template.render({},request))
	else:
		template = loader.get_template('anonuser.html')
		return HttpResponse(template.render({},request))
def getTargetedNews(request):
	link = "https://www.google.co.uk/finance/company_news?q=LON:VOD&output=rss"
	#print (top_headlines)
	conn = psycopg2.connect(dbname="gyesfxht", user="gyesfxht", password="VwftaOkFDwF2LoGElDUxJ7i4kjJyALvy", host="stampy.db.elephantsql.com", port="5432")
	cur.execute('SELECT * from "home_asset" WHERE "playerID" = %s', [current_user.id])
	x = cur.fetchone
	ticker = x[1]
	print (ticker)
	return render(request, 'home.html', {'ticker': ticker})

def mission(request):
	template = loader.get_template('mission.html')
	return HttpResponse(template.render({},request))
def anonuser(request):
	template = loader.get_template('anonuser.html')
	return HttpResponse(template.render({},request))
def settings(request):
	template = loader.get_template('settings.html')
	return HttpResponse(template.render({},request))
def awards(request):
	template = loader.get_template('awards.html')
	return HttpResponse(template.render({},request))
def receipt(request):
	template = loader.get_template('receipt.html')
	return HttpResponse(template.render({},request))
def leaderboard(request, league_id):
	template = loader.get_template('leaderboard.html')
	return HttpResponse(template.render({},request))
def processInvalid(request):
	template = loader.get_template('processInvalid.html')
	return HttpResponse(template.render({},request))
# Create your views here.
def shop(request):
	return render(request, 'shop.html', {})
@csrf_exempt
def submitShop(request,item):

	
	if item == 1:
		
		request.user.profile.TitanCoins = request.user.profile.TitanCoins + 100
	elif item == 2:
		
		request.user.profile.TitanCoins = request.user.profile.TitanCoins + 200
	elif item == 3:
		
		request.user.profile.TitanCoins = request.user.profile.TitanCoins + 300
	elif item == 4:
		
		if (request.user.profile.TitanCoins<100):
			return HttpResponseRedirect('/dashboard')
		request.user.profile.TitanCoins = request.user.profile.TitanCoins + 300

	print(request.user.profile.TitanCoins)
	return HttpResponseRedirect('/dashboard')