from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('payment/<int:order_id>/', views.payment, name='payment'),
]
