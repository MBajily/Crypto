from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Coin(models.Model):
    symbol = models.CharField(max_length=6, unique=True)


class BuySellHistory(models.Model):
    types = {
        ('Sell','Sell'),
        ('Buy', 'Buy')
    }
    amount = models.FloatField()
    price = models.FloatField()
    date = models.DateTimeField(auto_now=True)
    profit = models.FloatField()
    coin = models.ForeignKey(Coin, null=True, on_delete=models.SET_NULL)
    type = models.TextField(choices=types)
    trader = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class FavoriteCoin(models.Model):
    coin = models.ForeignKey(Coin, null=True, on_delete=models.CASCADE)
    trader = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Portfolio(models.Model):
    coin = models.ForeignKey(Coin, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField()


class Transaction(models.Model):
    coin = models.ForeignKey(Coin, null=False, on_delete=models.CASCADE)
    amount = models.FloatField()
    sender = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='receiver')
    date = models.DateTimeField(auto_now=True)
    note = models.TextField(max_length=100)

