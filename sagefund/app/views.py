from django.shortcuts import render

from .models import Transaction

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dashboard1.html')

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transactions.html', {'transactions': transactions})