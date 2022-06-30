from django.shortcuts import render, redirect
from requests import Request, Session
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
import json
import pprint

# Create your views here.

@login_required
def Dashboard(request):
    return render(request, 'index.html')


@login_required
def CoinDetails(request, symbol):
    coin = Coin.objects.get(symbol=symbol)
    getCoin = coin

    context = {'title':''}
    return render(request, 'coin-details.html', context)


@login_required
def Portfolio(request):
    trader = request.user
    portfolio = Portfolio.objects.filter(trader=trader).all()
    history = BuySellHistory.objects.filter(trader=trader).all()
    
    context = {'title':'', 'portfolio':portfolio, 'history':history}
    return render(request, 'portfolio.html', context)


@login_required
def Transactions(request):
    trader = request.user
    transactions = Transaction.objects.filter(Q(receiver=trader) | Q(sender=trader)).order_by('-date')

    context = {'title':'', 'transactions':transactions}
    return render(request, 'transactions.html', context)


@login_required
def MarketCap(request):
    coins = Coin.objects.all()

    context = {'title':'', 'coins':coins}
    return render(request, 'market-capital.html', context)