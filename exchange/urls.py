from django.contrib import admin
from django.urls import path, include
from . import views
from . import coinmarketcap

urlpatterns = [
    path('dashboard/', views.Dashboard, name="Dashboard"),
    path('<str:symbol>/details/', views.CoinDetails, name="CoinDetails"),
    path('transactions/', views.Transactions, name="Transactions"),
    path('market-capital/', views.MarketCap, name="MarketCap"),

    # APIs
    path('api/get-coin/<str:symbol>/', coinmarketcap.getCoin, name="getCoin"),
    path('api/get-market-capital/', coinmarketcap.getMarketCap, name="getMarketCap"),
    path('api/get-list-coins/', coinmarketcap.getListCoins, name="getListCoins"),
    path('api/get-top-gainers/', coinmarketcap.getTopGainers, name="getTopGainers"),
    path('api/get-top-losers/', coinmarketcap.getTopLosers, name="getTopLosers"),
]
