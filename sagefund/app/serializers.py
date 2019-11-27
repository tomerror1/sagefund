from rest_framework import serializers
from .models import Transaction, Deposit_history

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class Deposit_history_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit_history
        fields = '__all__'