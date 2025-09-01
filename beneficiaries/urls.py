from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BeneficiaryViewSet, BeneficiaryListView

router = DefaultRouter()
router.register(r'', BeneficiaryViewSet, basename='beneficiary')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', BeneficiaryListView.as_view(), name='beneficiary-list'),
]