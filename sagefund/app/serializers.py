from rest_framework import serializers
from .models import (
    Transaction, 
    Deposit_history, 
    Portfolio_securities, 
    Deposit_Securities,
    Asset,
)

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class Deposit_history_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit_history
        fields = '__all__'

class Portfolio_securities_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio_securities
        fields = '__all__'

class KPI_Serializer(serializers.ModelSerializer):
    value_of_asset = serializers.SerializerMethodField('calculate_value_of_asset')

    def calculate_value_of_asset(self, Deposit_Securities):
        value_of_asset = Deposit_Securities.shares * Deposit_Securities.asset.current_price    
        return round(value_of_asset, 2)

    class Meta:
        model = Deposit_Securities
        fields = ('asset', 'value_of_asset')