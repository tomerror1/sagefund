from rest_framework import routers
from app.viewsets import TransactionViewSet, Deposit_history_ViewSet

router = routers.DefaultRouter()

router.register(r'app', TransactionViewSet)

router.register(r'deposit_history', Deposit_history_ViewSet)