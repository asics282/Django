from django.urls import path
from .views import OrderListView, create_product

urlpatterns = [
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('create_product/', create_product, name='create_product'),
]
