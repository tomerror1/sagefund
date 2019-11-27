from rest_framework import viewsets
from .models import Transaction, Deposit_history
from .serializers import TransactionSerializer, Deposit_history_Serializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class Deposit_history_ViewSet(viewsets.ModelViewSet):
    queryset = Deposit_history.objects.all().order_by('date')
    serializer_class = Deposit_history_Serializer