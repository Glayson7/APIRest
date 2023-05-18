from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('cart', views.CartViewSet)
router.register('cart-items', views.CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
