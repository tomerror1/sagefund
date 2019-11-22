from django.shortcuts import render

from .models import Deposit, Asset, Deposit_Securities, Transaction, Portfolio, Portfolio_securities

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dashboard1.html')

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transactions.html', {'transactions': transactions})

def portfolio_buy(request):
    investment = 1000
    deposit = Deposit.objects.filter(number=1001).get()
    securities = Portfolio_securities.objects.all()
    for security in securities:
        Deposit_Securities.objects.create(deposit=deposit, asset=security.asset, shares=((security.percentage)*float(investment)))
    return render(request, 'home.html')