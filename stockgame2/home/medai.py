import numpy as np
import random
import math
from financepi import *
import time
from listofstockscrypto import *

def getLastMonth(item):
	df = getPriceFromAPI_m(item,False)
	i = 0
	data = np.array([])
	while i<df.shape[0]:
		data = np.append(data,[i+1,df['Open'][i]])	
		i+=1
	print (data)
	return
	
#list = getDow()
#lenList = len(list)
#for item in list:
#	getLastMonth(item)
