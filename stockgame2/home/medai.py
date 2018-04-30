import numpy as np
import math
from home.financepi import *
#from financepi import *
import time
from home.listofstockscrypto import *
#from listofstockscrypto import *
#import matplotlib.pyplot as plt
#import matplotlib.lines as mlines
import tensorflow as tf
import random
import math

def getLastMonth(item):
	df = getPriceFromAPI_m(item,False)
	i = 0
	data = np.zeros(shape=(df.shape[0],2))
	while i<df.shape[0]:
		x = np.array([i+1,df['Close'][i]])
		#print(data)
		#print(x)
		data[i] = x
		i+=1
	#print (data)
	return data

#list = getDow()
#lenList = len(list)
#for item in list:
#	getLastMonth(item)

def runLinearReg(data):
	# read data
	n_samples = len(data) - 1

	X = tf.placeholder(tf.float32, name="X")
	Y = tf.placeholder(tf.float32, name="Y")

	w = tf.Variable(0.0, name="weights")
	b = tf.Variable(0.0, name="bias")

	Y_predicted = X * w + b

	loss = tf.square(Y - Y_predicted, name="loss")

	optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)
	loss_sum = 0;
	count = 0;
	loss_perIndex = [0]*42;
	with tf.Session() as sess:
	    sess.run(tf.global_variables_initializer())

	    for i in range(100): # run 100 epochs
	        for ind, [x, y] in enumerate(data):
	            _, loss_val = sess.run([optimizer, loss], feed_dict={X: x, Y:y})
	            loss_perIndex[ind] = loss_perIndex[ind] + loss_val;
	            loss_sum += loss_val;
	            count += 1;
	    w_value, b_value = sess.run([w, b])

	    avg_loss = loss_sum/count

	    avgLossPerIndex = [1]*42;
	    for i in range(42):
	        avgLossPerIndex[i] = loss_perIndex[i]/10;

	return w_value, b_value,avg_loss


def getBuy_med(buyingPower):
	list = getDow()
	hi_score = [-10000000,-10000000,-10000000]
	w_3 = [0, 0, 0]
	loss_3 = [0, 0, 0]
	hi_item = ['blank','blank','blank']
	for item in list:
		data = getLastMonth(item)
		[w,b,loss] = runLinearReg(data)
		print("[BUY] " + item + ": " + str(w) +" "+ str(b) + " " + str(loss))
		score = w*1000/loss
		if score>hi_score[0]:
			hi_score[2]=hi_score[1]
			hi_score[1]=hi_score[0]
			hi_score[0]=score
			hi_item[2]=hi_item[1]
			hi_item[1]=hi_item[0]
			hi_item[0]=item
			w_3[2] = w_3[1]
			w_3[1]=w_3[0]
			w_3[0]=w
			loss_3[2] = loss_3[1]
			loss_3[1]=loss_3[0]
			loss_3[0]=loss

		elif score>hi_score[1]:
			hi_score[2]=hi_score[1]
			hi_score[1]=score
			hi_item[2]=hi_item[1]
			hi_item[1]=item
			w_3[2] = w_3[1]
			w_3[1]=w
			loss_3[2] = loss_3[1]
			loss_3[1]=loss
		elif score>hi_score[2]:
			hi_score[2]=score
			hi_item[2]=item
			w_3[2]=w
			loss_3[2]=loss
	randIndex = random.randint(0, 2)
	buy_item = hi_item[randIndex]
	weight = w_3[randIndex]
	loss = loss_3[randIndex]
	price = getPriceFromAPI(buy_item, False)
	rangeNumToBuy = math.floor(abs(0.25*float(buyingPower)/float(price)))
	randBuyNum = random.randint(1, rangeNumToBuy)
	return [buy_item, randBuyNum, weight, loss]

def getSell_med(currAssets, currAmts):
	if not currAssets:
		return 'none123', 0
	lo_score = 10000000
	lo_items = 'blank'
	index = 0
	lo_index = 0
	for item in currAssets:
		data = getLastMonth(item)
		[w,b,loss] = runLinearReg(data)
		print("[SELL] " + item + ": " + str(w) +" "+ str(b) + " " + str(loss))
		score = w*1000/loss
		if score<lo_score:
			lo_score = score
			lo_item = item
			lo_index = index
		index+=1
	randNumToSell = random.randint(1, currAmts[lo_index])
	return [lo_item, randNumToSell]
