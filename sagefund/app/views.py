from django.shortcuts import render

from .models import Deposit, Asset, Deposit_Securities, Transaction, Portfolio, Portfolio_securities

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dashboard1.html')

def calculate_value_of_deposit(request):
    value_of_deposit = 0
    deposit = Deposit_Securities.objects.all()
    for asset in deposit:
        value_of_deposit += asset.shares * asset.asset.current_price    
    print(value_of_deposit)
    return render(request, 'home.html')

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transactions.html', {'transactions': transactions})

def portfolio_buy(request):
    investment = 1000
    deposit = Deposit.objects.filter(number=1001).get()
    securities = Portfolio_securities.objects.all()
    order_type = "buy"
    for security in securities:
        # create an asset in deposit for every asset in Portfolio
        Deposit_Securities.objects.create(
            deposit=deposit, 
            asset=security.asset, 
            shares=((float(investment)*(security.percentage)/security.asset.current_price)),
        )
        # create the transactions
        Transaction.objects.create(
            asset=security.asset,
            order_type=order_type,
            # shares from above
            shares=((float(investment)*(security.percentage)/security.asset.current_price)),
            price=security.asset.current_price,
            # value = shares*price
            value=((float(investment)*(security.percentage)/security.asset.current_price))*security.asset.current_price,
            deposit=deposit,
        )
    return render(request, 'home.html')