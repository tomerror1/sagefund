from rest_framework import routers
from app.viewsets import TransactionViewSet

router = routers.DefaultRouter()

router.register(r'app', TransactionViewSet)