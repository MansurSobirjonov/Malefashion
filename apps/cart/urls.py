from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('add-cart/', add_cart, name='add-cart'),
    path('add-wishlist/', add_wishlist, name='add-wishlist'),
    path('my-cart/', my_cart, name='my-cart'),
    path('my-wishlist/', my_wishlist, name='my-wishlist'),
    path('plus-quantity/', plus_quantity, name='plus-quantity'),
    path('minus-quantity/', minus_quantity, name='minus-quantity'),
    path('delete-item/', delete_cart_item, name='delete-item'),
    path('checkout/', checkout, name='checkout'),
]
