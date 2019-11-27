from rest_framework import viewsets
from .models import (
    Transaction, 
    Deposit_history, 
    Portfolio_securities,
    Deposit_Securities,
)
from .serializers import (
    TransactionSerializer, 
    Deposit_history_Serializer, 
    Portfolio_securities_Serializer, 
    KPI_Serializer,
)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class Deposit_history_ViewSet(viewsets.ModelViewSet):
    queryset = Deposit_history.objects.all().order_by('date')
    serializer_class = Deposit_history_Serializer

class Portfolio_securities_ViewSet(viewsets.ModelViewSet):
    queryset = Portfolio_securities.objects.all().order_by('-percentage')
    serializer_class = Portfolio_securities_Serializer

class KIP_ViewSet(viewsets.ModelViewSet):
    queryset = Deposit_Securities.objects.all()
    serializer_class = KPI_Serializer