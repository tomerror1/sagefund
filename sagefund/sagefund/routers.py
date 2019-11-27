from rest_framework import routers
from app.viewsets import TransactionViewSet, Deposit_history_ViewSet, Portfolio_securities_ViewSet

router = routers.DefaultRouter()

router.register(r'app', TransactionViewSet)
router.register(r'deposit_history', Deposit_history_ViewSet)
router.register(r'portfolio_securities', Portfolio_securities_ViewSet)
