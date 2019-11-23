from datetime import datetime 

from django.db import models

from django.conf import settings

class Deposit(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='customer',)
    number = models.IntegerField()
    deposit_name = models.CharField(max_length=255)

    def __str__(self):
        return self.deposit_name

class Asset(models.Model):
    isin = models.CharField(max_length=12)
    wkn = models.CharField(max_length=6)
    type_of_asset = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    current_price = models.FloatField()
    tracking_index = models.CharField(max_length=255)
    sustainability_raiting = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Deposit_Securities(models.Model):
    deposit = models.ForeignKey(
        Deposit,
        on_delete=models.CASCADE,
    )
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
    )
    shares = models.FloatField()

    def __str__(self):
        return self.asset_ISIN


class Transaction(models.Model):
    date_of_transaction = models.DateTimeField(default=datetime.now)
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
    )
    order_type = models.CharField(max_length=12)
    shares = models.FloatField()
    price = models.FloatField()
    fees = models.FloatField(default=0)
    value =  models.FloatField()
    deposit = models.ForeignKey(
        Deposit,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.asset


class Portfolio(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Portfolio_securities(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
    )
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
    )
    percentage = models.FloatField()
    
    def __str__(self):
        return f'{self.asset.name}, {str(self.percentage)}%'
   
class Deposit_history(models.Model):
    deposit = models.ForeignKey(
        Deposit,
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    value_of_deposit = models.FloatField()

    def __str__(self):
        return f'{self.deposit.number}, {str(self.date)}, {str(self.value_of_deposit)} EUR'
