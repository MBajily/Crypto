from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('<str:symbol>/details/', views.CoinDetails, name="CoinDetails"),
]
