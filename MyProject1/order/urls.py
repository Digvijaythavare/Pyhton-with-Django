from django.urls import path
from . import views

urlpatterns = [
    path('', views.Sell, name='order-sell'),
    path('purchase/', views.Purchase, name='order-purchase'),
]