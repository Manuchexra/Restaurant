# joytop/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PaymentMethodViewSet, TableViewSet, UserRoleViewSet, UserViewSet, 
    OrderViewSet, MenuItemViewSet, CheckViewSet, TransactionViewSet, 
    ReportViewSet, DiscountViewSet, ReservationViewSet, FeedbackViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Router yaratish va barcha ViewSet'larni ro'yxatga olish
router = DefaultRouter()
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'tables', TableViewSet)
router.register(r'user-roles', UserRoleViewSet)
router.register(r'users', UserViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'checks', CheckViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
