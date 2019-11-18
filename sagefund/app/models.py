from django.db import models

from django.conf import settings

class Deposit(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='customer',)
    number = models.IntegerField()

    def __str__(self):
        return self.number


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
    deposit = models.OneToOneField(
        Deposit,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
    )
    shares = models.FloatField()

    def __str__(self):
        return self.asset_ISIN


class Transaction(models.Model):
    asset = models.CharField(max_length=255)
    volume =  models.IntegerField()
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
    percentage = models.IntegerField()
    
    def __str__(self):
        return self.asset
   
