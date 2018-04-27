from listofstockscrypto import *
from aiscripts import *
from financepi import *
from medai import *

def getBuy_hard():
	list = getDow()
	hi_score = -10000000
	hi_item = 'blank'
	for item in list:
		pos, neg, neut, tnum = getTwitterSentiments(item)
		if neg == 0:
			neg = 1
		if tnum == 0:
			twit_score = 1
		else:
			twit_score = pos/neg
		
		data = getLastMonth(item)
		[w,b,loss] = runLinearReg(data)
		linreg_score = w*1000/loss
		
		pos, neg, neut, lnum = getNewsSentiments(item)
		if neg == 0:
			neg = 1
		if lnum == 0:
			news_score = 1
		else:
			news_score = pos/neg
		
		tot_score = twit_score*linreg_score*news_score
		if tot_score>hi_score:
			hi_score = tot_score
			hi_item = item
	return hi_item
	
def getSell_hard(list):
	#list = getDow()
	lo_score = 1000000000
	lo_item = 'blank'
	for item in list:
		pos, neg, neut, tnum = getTwitterSentiments(item)
		if neg == 0:
			neg = 1
		if tnum == 0:
			twit_score = 1
		else:
			twit_score = pos/neg
		
		data = getLastMonth(item)
		[w,b,loss] = runLinearReg(data)
		linreg_score = w*1000/loss
		
		pos, neg, neut, lnum = getNewsSentiments(item)
		if neg == 0:
			neg = 1
		if lnum == 0:
			news_score = 1
		else:
			news_score = pos/neg
		
		tot_score = twit_score*linreg_score*news_score
		if tot_score<lo_score:
			lo_score = tot_score
			lo_item = item
	return lo_item
	