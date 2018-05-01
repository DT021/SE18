from home.listofstockscrypto import *
from home.aiscripts import *
from home.financepi import *
from home.medai import *
import math
import random

def getBuy_hard(buyingPower):
	list = getDow()
	hi_score = [-10000000,-10000000,-10000000]
	hi_item = ['blank','blank','blank']
	for item in list:
		try:
			pos, neg, neut, tnum, ptweets, ntweets = getTwitterSentiments(item)
			if neg == 0:
				neg = 1
			if tnum == 0:
				twit_score = 1
			else:
				twit_score = pos/neg
		except:
			twit_score=1
		data = getLastMonth(item)
		[w,b,loss] = runLinearReg(data)
		linreg_score = w*1000/loss
		try:
			pos, neg, neut, lnum, pnews, nnews = getNewsSentiments(item)
			if neg == 0:
				neg = 1
			if lnum == 0:
				news_score = 1
			else:
				news_score = pos/neg
		except:
			news_score = 1
		print("[BUY] " + item + ": " + str(w) +" "+ str(b) + " " + str(loss))
		print("		 " + item + ": " + str(pos) +" "+ str(neg) + " " + str(neut))
		tot_score = twit_score*linreg_score*news_score

		if tot_score>hi_score[0]:
			hi_score[2]=hi_score[1]
			hi_score[1]=hi_score[0]
			hi_score[0]=tot_score
			hi_item[2]=hi_item[1]
			hi_item[1]=hi_item[0]
			hi_item[0]=item
		elif tot_score>hi_score[1]:
			hi_score[2]=hi_score[1]
			hi_score[1]=tot_score
			hi_item[2]=hi_item[1]
			hi_item[1]=item
		elif tot_score>hi_score[2]:
			hi_score[2]=tot_score
			hi_item[2]=item
	buy_item = hi_item[random.randint(0, 2)]
	price = getPriceFromAPI(buy_item, False)
	rangeNumToBuy = math.floor(abs(0.25*float(buyingPower)/float(price)))
	randBuyNum = random.randint(1, rangeNumToBuy)
	print(ptweets)
	return [buy_item, randBuyNum, ptweets, ntweets, pnews, nnews]

def getSell_hard(currAssets, currAmts):
	if not currAssets:
		return 'none123', 0
	lo_score = 1000000000
	lo_item = 'blank'
	index = 0
	lo_index = 0
	for item in currAssets:
		pos, neg, neut, tnum, ptweets, ntweets = getTwitterSentiments(item)
		if neg == 0:
			neg = 1
		if tnum == 0:
			twit_score = 1
		else:
			twit_score = pos/neg

		data = getLastMonth(item)
		[w,b,loss] = runLinearReg(data)
		linreg_score = w*1000/loss

		pos, neg, neut, lnum, pnews, nnews = getNewsSentiments(item)
		if neg == 0:
			neg = 1
		if lnum == 0:
			news_score = 1
		else:
			news_score = pos/neg

		print("[SELL] " + item + ": " + str(w) +" "+ str(b) + " " + str(loss))
		print("		 " + item + ": " + str(pos) +" "+ str(neg) + " " + str(neut))

		tot_score = twit_score*linreg_score*news_score
		if tot_score<lo_score:
			lo_score = tot_score
			lo_item = item
			lo_index = index
		index+=1
	randNumToSell = random.randint(1, currAmts[lo_index])
	return [lo_item, randNumToSell]
