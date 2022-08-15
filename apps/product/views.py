from django.shortcuts import render, redirect
from apps.blog.models import Post
from apps.contact.models import Subscribe
from .models import *


# Create your views here.


def home(request):
    posts = Post.objects.order_by('-id')
    email = request.GET.get('email')
    if email:
        Subscribe.objects.create(email=email)
        return redirect('.')
    products = Product.objects.order_by('-id')
    s = request.GET.get('s')
    if s:
        products = products.filter(name__icontains=s)
    ctx = {
        'posts': posts,
        'products': products,
        'l': [0, 1, 2, 3, 4]
    }
    return render(request, 'index.html', ctx)


def shop(request):
    products = Product.objects.order_by('-id')
    ema = request.GET.get('email')
    if ema:
        Subscribe.objects.create(email=ema)
        return redirect('.')
    categories = Category.objects.all()
    ctx = {
        'products': products,
        'categories': categories,
        'l': [0, 1, 2, 3, 4]
    }
    return render(request, 'shop.html', ctx)


def shop_details(request, pk):
    product = Product.objects.get(id=pk)
    related_products = Product.objects.order_by('-id')[:4]
    ctx = {
        'product': product,
        'related_products': related_products,
        'l': [0, 1, 2, 3, 4]
    }
    return render(request, 'shop-details.html', ctx)
