from django.shortcuts import render, redirect
from requests import Request, Session
from .models import *
import json
import pprint
# Create your views here.

def dashboard(request):
    return render(request, 'index.html')


def CoinDetails(request, symbol):
    coin = Coin.objects.get(symbol=symbol)
    getCoin = coin
    context = {'title':getCoin}
    return render(request, 'coin-details.html', context)