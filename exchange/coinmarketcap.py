from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from .models import Coin
import json
import pprint


headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'7cjkjjc0a-f009-4889-8938-akhbkjbjkbkj1fc'
}

session = Session()
session.headers.update(headers)


# Function to get coin information (getCoin).
def getCoin(symbol):
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'  
    parameters = {
        'symbol':symbol,
        'convert':'USD'
    }

    try:
        response = session.get(url, params=parameters)
        return json.loads(response.text).data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


# Function to get list of market cap (getMarketCap).
	# Available coins in platform
	# Return list of coins order by marketcap

def getMarketCap(start, limit, sort, sort_dir, convert):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':start,
        'limit':limit,
        'sort':sort,
        'sort_dir':sort_dir,
        'convert':convert
    }

    try:
        response = session.get(url, params=parameters)
        return json.loads(response.text).data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def getListCoins(symbols):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    response = []

    for symbol in symbols:
        response.append(getCoin(symbol))

    return json.loads(response)
    


def getTopGainers():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':1,
        'limit':5,
        'sort':'percent_change_24h',
        'sort_dir':'asc',
        'percent_change_24h_min':0
    }

    try:
        response = session.get(url, params=parameters)
        return json.loads(response.text).data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def getTopLosers():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':1,
        'limit':5,
        'sort':'percent_change_24h',
        'sort_dir':'desc',
        'percent_change_24h_max':0
    }

    try:
        response = session.get(url, params=parameters)
        return json.loads(response.text).data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)