from django.shortcuts import render, redirect
from requests import Request, Session
from django.contrib.auth.decorators import login_required
from .models import *
import json
import pprint

# Create your views here.

@login_required()
def Dashboard(request):
    return render(request, 'index.html')


@login_required()
def CoinDetails(request, symbol):
    coin = Coin.objects.get(symbol=symbol)
    getCoin = coin

    context = {'title':''}
    return render(request, 'coin-details.html', context)


@login_required()
def Portfolio(request):
    trader = request.user
    wallet = Wallet.objects.filter(trader=trader).all()
    history = BuySellHistory.objects.filter(trader=trader).all()
    context = {'title':''}
    return render(request, 'portfolio.html', context)