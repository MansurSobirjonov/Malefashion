from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', blog, name='blog'),
    path('blog-single/<int:pk>/', blog_single, name='blog_single'),
]
