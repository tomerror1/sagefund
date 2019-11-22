from django.conf.urls import url

from . import views

urlpatterns = [
    url('dashboard', views.dashboard),
    url('transactions', views.transaction_list),
    url('portfolio_buy', views.portfolio_buy),
]