from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.Dashboard, name="Dashboard"),
    path('<str:symbol>/details/', views.CoinDetails, name="CoinDetails"),
    path('transactions/', views.Transactions, name="Transactions"),
]
