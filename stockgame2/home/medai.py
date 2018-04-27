import numpy as np
import math
from financepi import *
import time
from listofstockscrypto import *
#import matplotlib.pyplot as plt
#import matplotlib.lines as mlines
import tensorflow as tf

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

	# Step 2: create placeholders for input X (number of fire) and label Y (number of theft)
	X = tf.placeholder(tf.float32, name="X")
	Y = tf.placeholder(tf.float32, name="Y")

	# Step 3: create weight and bias, initialized to 0
	w = tf.Variable(0.0, name="weights")
	b = tf.Variable(0.0, name="bias")

	# Step 4: construct model to predict Y (number of theft) from the number of fire
	Y_predicted = X * w + b

	# Step 5: use the square error as the loss function
	loss = tf.square(Y - Y_predicted, name="loss")

	# Step 6: using gradient descent with learning rate of 0.01 to minimize loss
	optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)
	loss_sum = 0;
	count = 0;
	loss_perIndex = [0]*42;
	with tf.Session() as sess:
		# Step 7: initialize the necessary variables, in this case, w and b
	    sess.run(tf.global_variables_initializer())

	    # Step 8: train the model
	    for i in range(100): # run 100 epochs
	        for ind, [x, y] in enumerate(data):
	            # Session runs train_op to minimize loss
	            _, loss_val = sess.run([optimizer, loss], feed_dict={X: x, Y:y})
	            loss_perIndex[ind] = loss_perIndex[ind] + loss_val;
	            loss_sum += loss_val;
	            count += 1;
	    # Step 9: output the values of w and b
	    w_value, b_value = sess.run([w, b])

	    avg_loss = loss_sum/count

	    avgLossPerIndex = [1]*42;
	    for i in range(42):
	        avgLossPerIndex[i] = loss_perIndex[i]/10;

	    #print(avg_loss)
	    #print(w_value)
	    #print(b_value)
	return w_value, b_value,avg_loss



	# Step 10: plot values
	#dataX = list()
	#dataY = list()
	#regressedData = list()

	# Get original data elements
	#for pair in data:
	 #   dataX.append(pair[0])
	  #  dataY.append(pair[1])

	#plt.scatter(dataX, avgLossPerIndex);
def getBuy_med():
	list = getDow()
	hi_score = -10000000
	hi_item = 'blank'
	for item in list:
		data = getLastMonth(item)
		[w,b,loss] = runLinearReg(data)
		score = w*1000/loss
		if score>hi_score:
			hi_score = score
			hi_item = item
	#print([hi_item,hi_score])
	return hi_item
def getSell_med(list):
	#list = getDow()
	lo_score = 10000000
	lo_item = 'blank'
	for item in list:
		data = getLastMonth(item)
		[w,b,loss] = runLinearReg(data)
		score = w*1000/loss
		if score<hi_score:
			lo_score = score
			lo_item = item
	#print([hi_item,hi_score])
	return lo_item