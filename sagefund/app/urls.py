from django.conf.urls import url

from . import views

urlpatterns = [
    url('dashboard', views.dashboard),
    url('transactions', views.transaction_list),
    url('portfolio_buy', views.portfolio_buy),
    url('calculate_value_of_deposit', views.calculate_value_of_deposit),
    url('calculate_performance_of_deposit', views.calculate_performance_of_deposit),
    url('index', views.index),
]