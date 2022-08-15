from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('shop-details/<int:pk>/', shop_details, name='shop-details'),
]
