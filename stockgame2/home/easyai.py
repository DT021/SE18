import random
import math
from home.financepi import *
from home.listofstockscrypto import *
import time
import decimal

def easyAI(isCrypto, buyingPower, currAssets, currAmts):

  # BUY
  # dow jones stocks
  if isCrypto == False:
    list = getSP500()
  else:
    list = getCryptoList()

  lenList = len(list)

  ################ BUY ORDER
  randBuyStock = list[random.randint(0, lenList-1)]
  percent = 0.15 # random percent to choose how many stocks to buy or sell

  if isCrypto == False:
      price = getPriceFromAPI(randBuyStock, isCrypto)
  else:
      price = getCryptoPriceFromAPI(randBuyStock, isCrypto)

  iter = 0;

  # invalid call possible if API doesn't have currency
  buyIndex = 1
  while (price == -1 and iter < 25):
      iter = iter + 1
      buyIndex = random.randint(0, lenList-1)
      randBuyStock = list[buyIndex]
      if isCrypto == False:
          price = getPriceFromAPI(randBuyStock, isCrypto)
      else:
          price = getCryptoPriceFromAPI(randBuyStock, isCrypto)
      if (price == -22): # -22 indicates too many api calls, sleep
          time.sleep(2)

  # checks if reached max iteration
  if (iter >= 25): # reaches max iteration
    if (isCrypto == False):
        randBuyStock = 'GOOGL'
        randBuyNum = 1
        buyIndex = 1
    else:
        randBuyStock = 'BTC'
        randBuyNum = 1
        buyIndex = 1
  else: # has a valid price because has not reached max iter
      if price == 0:
        price = 10
      rangeNumToBuy = math.floor(abs(float(percent)*float(buyingPower)/float(price)))
      randBuyNum = random.randint(0, rangeNumToBuy)

  ################ SELL ORDER
  lenAssets = len(currAssets)
  if lenAssets == 0:
    return [randBuyStock, randBuyNum, 'none123', 0]
  randInd =random.randint(0, lenAssets-1)
  randSellStock = currAssets[randInd]
  randNumToSell = random.randint(0, currAmts[randInd])

  return [randBuyStock, randBuyNum, randSellStock, randNumToSell, buyIndex]

#print(easyAI(False, 1000000, ['abc', 'fgb', 'lmf'], [5, 20, 30]))
