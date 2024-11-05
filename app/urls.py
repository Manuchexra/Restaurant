# restaurant_payment/urls.py
from django.urls import path
from .views import (
    PaymentMethodListCreateAPIView,
    TableListCreateAPIView,
    CheckDetailAPIView,
    TransactionCreateAPIView,
    ReportListAPIView
)

urlpatterns = [
    path('payment_methods/', PaymentMethodListCreateAPIView.as_view(), name='payment_methods'),
    path('tables/', TableListCreateAPIView.as_view(), name='tables'),
    path('checks/<int:check_id>/', CheckDetailAPIView.as_view(), name='check_detail'),
    path('transactions/', TransactionCreateAPIView.as_view(), name='transaction_create'),
    path('reports/', ReportListAPIView.as_view(), name='reports'),
]
