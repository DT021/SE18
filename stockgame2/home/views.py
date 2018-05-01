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
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt
import decimal
import os

account_sid = "AC0442f02a5d307c7c2f9bb0b6d63d98b7"
try:
	auth_token = os.environ["TWILIO_SECRET"]
except KeyError:
	auth_token  = "x"


from django.contrib.postgres.fields import ArrayField

from django.views.decorators.csrf import csrf_exempt

from home.easyai import *
from home.medai import *
from home.hardai import *






client = Client(account_sid, auth_token)
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
			new_league = League(adminID = current_user.id,name=lname,numPlayers=1,joinPassword=joinpwd,startingBalance=startbal,isCrypto=b, endDate=date_out,isUniversal=False, hasEnded = False)
			new_league.save()
			newPlayer = Player(leagueID=new_league,userID=current_user, buyingPower = startbal,percentChange=0,totalWorth=0, cumWorth = startbal, isAi = False)
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
		isCrypto = league.isCrypto
		print(isCrypto)
		#buyingPrice = form.cleaned_data.get('buyingPrice')
		if isCrypto == True:
			buyingPrice = getCryptoPriceFromAPI2(ticker, True)
		else:
			buyingPrice = getPriceFromAPI(ticker,False) #allow crypto in future
		if buyingPrice == -1:
			storage = messages.get_messages(request)
			messages.add_message(request, messages.ERROR, 'Please enter a valid ticker. Cryptocurrency leagues only accept cryptocurrency.')
			storage.used = False
			return render(request, 'buypage.html', {'form': form,'league':league,'player':player})
		elif buyingPrice == -22:
			storage = messages.get_messages(request)
			messages.add_message(request, messages.ERROR, 'Too many requests at this time.')
			storage.used = False
			return render(request, 'buypage.html', {'form': form,'league':league,'player':player})
		elif buyingPrice <0:
			storage = messages.get_messages(request)
			messages.add_message(request, messages.ERROR, 'Invalid Input.')
			storage.used = False
			return render(request, 'buypage.html', {'form': form,'league':league,'player':player})
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
		try:
			message = client.messages.create(
				to="+17329985271",
				from_="+17325079667",
				body="You bought %d shares of %s at $%d!" % (shares,ticker,tmpPrice))
		except:
			pass
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
	league = lastTransaction.leagueID
	price = lastTransaction.price
	ticker = lastTransaction.ticker
	shares = lastTransaction.shares
	return render(request, 'receipt.html', {'price': price, 'ticker': ticker, 'shares': shares,'league':league})


def createai(request):
	form = CreateAiForm(request.POST)
	if(form.is_valid()):
		ainame = form.cleaned_data.get('ainame')
		leaguename = form.cleaned_data.get('leaguename')
		leagueSet = League.objects.filter(name=leaguename)
		league = leagueSet.first()
		userid = auth_User.objects.filter(username = ainame)
		print(userid)
		newPlayer = Player(leagueID=league,userID=userid.first(), buyingPower = league.startingBalance,percentChange=0,totalWorth=0,isAi=True, cumWorth = league.startingBalance)
		league.numPlayers+=1
		league.save()
		newPlayer.save()
		#url = '/leagues/'+str(league.id)+'/'
		return render(request, 'home.html')
	else:
		return render(request, 'home.html')



def aipage(request, league_id):

    # get ai player
    aiplayer = Player.objects.filter(leagueID = league_id, isAi = True)
    if not aiplayer:
        return redirect('/shop')

    l = aiplayer.first()

	# perform transactions
    count = 0

    currasset = list()
    curramt = list()
    result = list()
    easyBuyIndex = 0

    medweight = 0
    medbias = 0
    medloss = 0

    ptweets = []
    ntweets = []
    pnews = []
    nnews = []
    assething = Asset.objects.filter(leagueID = league_id)

    if l.userID.id == 3:
        for h in assething:
            if h.playerID == l.id:
                currasset.append(h.ticker)
                curramt.append(h.shares)
        result = easyAI(l.leagueID.isCrypto,l.buyingPower,currasset,curramt)
        print(result)
        shares = result[1]
        ticker = result[0]
        if shares != 0:
            buydash(ticker, shares,l.leagueID.id, l.id)
        if result[3] != 0:
            asset123 = Asset.objects.filter(ticker = result[2], playerID = l.id)
            selldash(result[3],l.id,l.leagueID.id,asset123.first().id)
        easyBuyIndex = result[4]
        diff = 1
        result.clear()
        currasset.clear()
        curramt.clear()

    if l.userID.id == 4:
        diff = 2
        for h in assething:
            if h.playerID == l.id:
                currasset.append(h.ticker)
                curramt.append(h.shares)
        result = getBuy_med(l.buyingPower)
        ticker = result[0]
        shares = result[1]
        medweight = result[2]
        medloss = result[3]
        if shares != 0:
            buydash(ticker, shares,l.leagueID.id, l.id)
        print(currasset)
        print(curramt)
        result.clear()
        result = getSell_med(currasset,curramt)
        ticker = result[0]
        shares = result[1]
        print(ticker)
        print(shares)
        if shares != 0:
            asset123 = Asset.objects.filter(ticker = ticker, playerID = l.id)
            selldash(shares,l.id,l.leagueID.id,asset123.first().id)
        currasset.clear()
        curramt.clear()

    if l.userID.id == 5:
        diff = 3
        for h in assething:
            if h.playerID == l.id:
                currasset.append(h.ticker)
                curramt.append(h.shares)
        result = getBuy_hard(l.buyingPower)
        ticker = result[0]
        shares = result[1]
        ptweets = result[2]
        ntweets = result[3]
        pnews = result[4]
        nnews = result[5]
        if shares != 0:
            buydash(ticker, shares,l.leagueID.id, l.id)
        print(currasset)
        print(curramt)
        result.clear()
        result = getSell_hard(currasset,curramt)
        ticker = result[0]
        shares = result[1]
        if shares != 0:
            asset123 = Asset.objects.filter(ticker = ticker, playerID = l.id)
            print(asset123)
            selldash(shares,l.id,l.leagueID.id,asset123.first().id)
        currasset.clear()
        curramt.clear()

    # query for changes in the database
    cumWorth = l.cumWorth
    buyingPower = l.buyingPower
    pTransactions = Transaction.objects.filter(playerID = l.id)
    print(pTransactions)
    pAssets = Asset.objects.filter(leagueID = league_id, playerID = l.id)
    print(pAssets)
    p, n, neutPercent, len, ptweets, ntweets = getTwitterSentiments(ticker)
    perPos, perNeg, perNeut, numAll, pnews, nnews = getNewsSentiments(ticker)

    return render(request, 'aipage.html', {'assets': pAssets, 'cumWorth': cumWorth, 'buyingPower': buyingPower, 'transactions': pTransactions, 'diff':diff,
    'easyBuyIndex':easyBuyIndex, 'medWeight':medweight, 'medLoss':medloss, 'ptweets':ptweets[:5], 'ntweets':ntweets[:5], 'pnews':pnews[:5], 'nnews':nnews[:5]})




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
			#marketPrice = getPriceFromAPI(asset.ticker, False)
			if league.isCrypto == True:
				marketPrice = getCryptoPriceFromAPI2(asset.ticker, True)
			else:
				marketPrice = getPriceFromAPI(asset.ticker,False) #allow crypto in future
			if marketPrice == -1:
				storage = messages.get_messages(request)
				messages.add_message(request, messages.ERROR, 'Please enter a valid ticker. Cryptocurrency leagues only accept cryptocurrency.')
				storage.used = False
				return render(request, 'sellform.html', {'form': form, 'league':league,'player':player,'asset':asset})
			elif marketPrice == -22:
				storage = messages.get_messages(request)
				messages.add_message(request, messages.ERROR, 'Too many requests at this time.')
				storage.used = False
				return render(request, 'sellform.html', {'form': form, 'league':league,'player':player,'asset':asset})
			elif marketPrice <0:
				storage = messages.get_messages(request)
				messages.add_message(request, messages.ERROR, 'Invalid Input.')
				storage.used = False
				return render(request, 'sellform.html', {'form': form, 'league':league,'player':player,'asset':asset})
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
			try:
				message = client.messages.create(
					to="+17329985271",
					from_="+17325079667",
					body="You sold %d shares of %s at $%d!" % (shares,ticker,tmpPrice))
			except:
				pass
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


		admin = list()
		rank = list()
		for p in players:
			count = 0
			people = Player.objects.filter(leagueID = p.leagueID).order_by('-cumWorth')
			# for i in people:
				# worth = 0
				# assets = Asset.objects.filter(playerID=i.id)
				# for a in assets:
						# marketPrice = getPriceFromAPI(a.ticker, p.leagueID.isCrypto)
						# worth+= (marketPrice*a.shares)
				# i.totalWorth = worth
				# i.cumWorth = i.totalWorth + i.buyingPower
				# i.save()
			# people = Player.objects.filter(leagueID = p.leagueID).order_by('-cumWorth')

			for l in people:
				count+=1
				if l.userID.id == p.leagueID.adminID:
					admin.append(l.userID.username)
				if l.userID.id == request.user.id:
					rank.append(count)


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
	for i in players:
		worth = 0
		assets = Asset.objects.filter(playerID=i.id)
		for a in assets:
				if league.isCrypto:
					marketPrice = getCryptoPriceFromAPI2(a.ticker, league.isCrypto)
				else:
					marketPrice = getPriceFromAPI(a.ticker, league.isCrypto)
				worth+= (marketPrice*a.shares)
		i.totalWorth = worth
		i.cumWorth = i.totalWorth + i.buyingPower
		i.save()
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
		if p.isAi and count > rank: # AI placing worse than user
			numAIbeat += 1
	if (endDate < presentDate): # league has ended, redirect to leaderboard.html
		if not (league.hasEnded): # need to handle trophies
			league.hasEnded = True
			current_user.profile.trophies[3] += 1 # increment for game played
			current_user.profile.TitanCoins += 50
			if rank < 4: # top 3 = win
				current_user.profile.trophies[2] += 1 # increment for win
				current_user.profile.TitanCoins += 100
			current_user.profile.trophies[4] = current_user.profile.trophies[4] + numAIbeat
			if numAIbeat>0:
				current_user.profile.TitanCoins += 25*numAIbeat
			if admin.id == request.user.id: # this user is admin
				if current_user.profile.trophies[5] < count: # new record for # ppl managed
					current_user.profile.trophies[5] = count
					current_user.profile.TitanCoins += 100
			current_user.save()
			#current_user.profile.TitanCoins +=
		return render(request, 'leaderboard.html', {'league': league, 'admin': admin, 'players':players,'currPlayer':currPlayer, 'rank':rank})

	pAssets = Asset.objects.filter(playerID = currPlayer.id)
	assetWorth = list()
	for a in pAssets:
		if league.isCrypto:
			marketPrice = getCryptoPriceFromAPI2(a.ticker, league.isCrypto)
		else:
			marketPrice = getPriceFromAPI(a.ticker, league.isCrypto)
		assetWorth.append(marketPrice*a.shares)
	#print(pAssets)

	return render(request, 'individualleague.html', {'league': league, 'admin': admin, 'players':players,'currPlayer':currPlayer,'pAssets':pAssets,'rank':rank,'assetWorth':assetWorth})

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


@csrf_exempt
def sms(request):
	league = League.objects.get(name="SoftwareEngineering")
	player = Player.objects.get(id=18)
	purchase = request.POST.get('Body', '')
	processed = purchase.split()
	print(processed)
	operation = processed[0]
	shares = processed[1]
	ticker = processed[2]
	if operation == "BUY":
		buyingPrice = getPriceFromAPI(ticker,False) #allow crypto in future
		tmpPrice = buyingPrice*decimal.Decimal(shares)
		message = '<Response><Message>You bought %s shares of %s for $%s</Message></Response>' % (shares,ticker, tmpPrice)
		if tmpPrice > player.buyingPower:
			return redirect('/home')
		new_asset = Asset(ticker = ticker, playerID = player.id, leagueID = league, shares = shares, buyingPrice = buyingPrice)
		new_asset.save()
		new_transaction = Transaction(leagueID = league, playerID = player.id, price = tmpPrice, ticker = ticker, shares = shares, isBuy = True)
		player.buyingPower = player.buyingPower-tmpPrice
		new_transaction.save()
		return HttpResponse(message, content_type='text/xml')

	if operation == "SELL":
		buyingPrice = getPriceFromAPI(ticker,False) #allow crypto in future
		tmpPrice = buyingPrice*decimal.Decimal(shares)
		asset = Asset.objects.get(ticker=ticker)
		message = '<Response><Message>You sold %s shares of %s for $%s</Message></Response>' % (shares,ticker, tmpPrice)
		currShares = asset.shares
		asset.shares = currShares - shares
		if asset.shares == 0:
			asset.delete()
		else:
			asset.save()
		player.buyingPower = player.buyingPower-tmpPrice
		new_transaction.save()
		return HttpResponse(message, content_type='text/xml')


# Create your views here.
@csrf_exempt
def shop(request):
	return render(request, 'shop.html', {})
@csrf_exempt
def submitShop(request,item):
	userprof = Profile.objects.get(user=request.user)
	if item == 1:

		userprof.TitanCoins=userprof.TitanCoins+100
		userprof.save()
		return HttpResponseRedirect('/dashboard')
	elif item == 2:

		userprof.TitanCoins=userprof.TitanCoins+500
		userprof.save()
		return HttpResponseRedirect('/dashboard')
	elif item == 3:

		userprof.TitanCoins=userprof.TitanCoins+1000
		userprof.save()
		return HttpResponseRedirect('/dashboard')
	elif item == 4:

		if (request.user.profile.TitanCoins<100):
			return HttpResponseRedirect('/dashboard')
		userprof.TitanCoins=userprof.TitanCoins-100
		userprof.save()
		return HttpResponseRedirect('/createaipage')
	elif item == 5:

		if (request.user.profile.TitanCoins<100):
			return HttpResponseRedirect('/dashboard')
		userprof.TitanCoins=userprof.TitanCoins-100
		userprof.save()
		return HttpResponseRedirect('/dashboard')
	elif item == 6:
		return HttpResponseRedirect('/dashboard')
	

