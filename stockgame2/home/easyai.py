import random
import math
from financepi import *
from listofstockscrypto import *
import time

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
  while (price == -1 and iter < 25):
      iter = iter + 1
      randBuyStock = list[random.randint(0, lenList-1)]
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
    else:
        randBuyStock = 'BTC'
        randBuyNum = 1
  else: # has a valid price because has not reached max iter
      rangeNumToBuy = math.floor(abs(percent*buyingPower/float(price)))
      randBuyNum = random.randint(0, rangeNumToBuy)

  ################ SELL ORDER
  lenAssets = len(currAssets)
  randInd =random.randint(0, lenAssets-1)
  randSellStock = currAssets[randInd]
  randNumToSell = random.randint(0, currAmts[randInd])

  return randBuyStock, randBuyNum, randSellStock, randNumToSell

print(easyAI(True, 1000, ['abc', 'fgb', 'lmf'], [5, 20, 30]))
