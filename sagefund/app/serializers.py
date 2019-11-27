from rest_framework import serializers
from .models import Transaction, Deposit_history, Portfolio_securities

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