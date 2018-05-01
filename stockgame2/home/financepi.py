import requests
import json
from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data
import decimal
# Utilizes Alpha Vantgae
#API KEY = TRKCXDZJRBBO0REH

def getPriceFromAPI(symbol, isCrypto):
	param = {
	'q': symbol, # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "NASD", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "1Y" # Period (Ex: "1Y" = 1 year)
	}

	df = get_price_data(param)
	if not df.empty:
		price = df['Open'][-1]
		return round(decimal.Decimal(price),2)
	param = {
	'q': symbol, # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "INDEXDJX", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "1Y" # Period (Ex: "1Y" = 1 year)
	}

	df = get_price_data(param)
	if not df.empty:
		price = df['Open'][-1]
		return round(decimal.Decimal(price),2)
		
	param = {
	'q': symbol, # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "INDEXSP", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "1Y" # Period (Ex: "1Y" = 1 year)
	}

	df = get_price_data(param)
	if not df.empty:
		price = df['Open'][-1]
		return round(decimal.Decimal(price),2)
		
	param = {
	'q': symbol, # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "NYSE", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "1Y" # Period (Ex: "1Y" = 1 year)
	}

	df = get_price_data(param)
	if not df.empty:
		price = df['Open'][-1]
		return round(decimal.Decimal(price),2)
	return -1
#print(getPriceFromAPI('GOOGL', False))

def getCryptoPriceFromAPI(symbol, isCrypto):
    APIKEY = 'TRKCXDZJRBBO0REH'

    # sets url based on if cryptocurrency or not
    if isCrypto == False:
        funct = 'TIME_SERIES_INTRADAY&interval=1min'
    else: #is cryptocurrency
        funct = 'DIGITAL_CURRENCY_INTRADAY'

    url = ('https://www.alphavantage.co/query?'
            'function='+funct+'&'
            'symbol='+symbol+'&'
            'market=USD&'
            'apikey='+APIKEY)

    response = requests.get(url)
    binary = response.content
    jsonData = json.loads(binary) #gets JSON data

    # Check if any errors, return -1
    if ('Error Message' in jsonData):
        return -1

    if ('Information' in jsonData):
        return -22

    # Dependent on JSON Format
    if isCrypto == False:
        timekey = 'Time Series (1min)'
        lastkey = '3. Last Refreshed'
        whichprice = '1. open'
    else:
        timekey = 'Time Series (Digital Currency Intraday)'
        lastkey = '7. Last Refreshed'
        whichprice = '1a. price (USD)'

    timeUpdates = jsonData[timekey]
    lastRefreshed = jsonData['Meta Data'][lastkey]
    recentPrices = timeUpdates[lastRefreshed]
    openPrice = recentPrices[whichprice]

	return round(decimal.Decimal(openPrice),2)

def getCryptoPriceFromAPI2(symbol,isCrypto):
	APIKEY = 'C1D9E9FC-4D44-4F52-BF51-7EA190BB4DBF'
	headers = {'X-CoinAPI-Key' : APIKEY}
	url ='https://rest.coinapi.io/v1/exchangerate/'+symbol+'/USD'

	response = requests.get(url, headers=headers)
	binary = response.content
	jsonData = json.loads(binary) #gets JSON data

	# Check if any errors, return -1
	if ('error' in jsonData):
		return -1
	price = jsonData['rate']
	print(price)
	return round(decimal.Decimal(price),2)
	
def getPriceFromAPI_m(symbol, isCrypto):
	param = {
	'q': symbol, # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "NASD", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "1M" # Period (Ex: "1Y" = 1 year)
	}

	df = get_price_data(param)
	if not df.empty:
		return df
	
	param = {
	'q': symbol, # Stock symbol (ex: "AAPL")
	'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
	'x': "NYSE", # Stock exchange symbol on which stock is traded (ex: "NASD")
	'p': "1M" # Period (Ex: "1Y" = 1 year)
	}

	df = get_price_data(param)
	if not df.empty:
		return df
	return -1

