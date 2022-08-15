from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from apps.contact.models import Subscribe
from .forms import OrderForm


# Create your views here.


@login_required
def add_cart(request):
    pid = request.GET.get('_pid')
    user = request.user
    product = Product.objects.get(id=pid)
    my_ct, new_cart = Cart.objects.get_or_create(user=user, is_ordered=False)
    data = None
    if my_ct:
        c = CartItem.objects.filter(product=product, cart=my_ct).count()
        if c < 1:
            CartItem.objects.create(product=product, cart=my_ct)
        else:
            q = CartItem.objects.get(product=product, cart=my_ct)
            q.quantity += 1
            q.save()
        data = {
            'success': True,
            'product': product.name,
            'message': 'successfully added your cart!'
        }
    elif new_cart:
        c = CartItem.objects.filter(product=product, cart=new_cart).count()
        if c < 1:
            CartItem.objects.create(product=product, cart=new_cart)
        else:
            q = CartItem.objects.get(product=product, cart=new_cart)
            q.quantity += 1
            q.save()
        data = {
            'success': True,
            'product': product.name,
            'message': 'successfully added your cart!'
        }
    return JsonResponse(data, status=201)


@login_required
def my_cart(request):
    try:
        cart = Cart.objects.get(user=request.user, is_ordered=False)
    except:
        pass
    e = request.GET.get('email')
    if e:
        Subscribe.objects.create(email=e)
        return redirect('.')
    ctx = {
        'cart': cart
    }
    return render(request, 'shopping-cart.html', ctx)


@login_required
def add_wishlist(request):
    pid = request.GET.get('_pid')
    user = request.user
    product = Product.objects.get(id=pid)
    wlc = Wishlist.objects.filter(user=user, product=product).count()
    if wlc < 1:
        Wishlist.objects.create(user=user, product=product)
        data = {
            'success': True,
            'product': product.name,
            'message': 'successfully added your wishlist!'
        }
    else:
        Wishlist.objects.get(user=user, product=product).delete()
        data = {
            'success': False,
            'product': product.name,
            'message': 'successfully removed from your wishlist!'
        }
    return JsonResponse(data, status=201)


@login_required
def my_wishlist(request):
    my_wl = Wishlist.objects.filter(user=request.user)
    e = request.GET.get('email')
    if e:
        Subscribe.objects.create(email=e)
        return redirect('.')
    ctx = {
        'products': my_wl
    }
    return render(request, 'my-wishlist.html', ctx)


def plus_quantity(request):
    ciid = request.GET.get('_ciid')
    item = CartItem.objects.get(id=ciid)
    item.quantity += 1
    item.save()
    data = {
        'success': True,
        'message': 'cart item incremented by 1',
    }
    return JsonResponse(data, status=200)


def minus_quantity(request):
    cid = request.GET.get('_ciid')
    item = CartItem.objects.get(id=cid)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
        data = {
            'success': True,
            'message': 'cart item decremented by 1'
        }
    else:
        item.delete()
        data = {
            'success': False,
            'message': 'cart item deleted'
        }
    return JsonResponse(data, status=200)


def delete_cart_item(request):
    cid = request.GET.get('_ciid')
    CartItem.objects.get(id=cid).delete()
    data = {
        'success': True,
        'message': 'cart item successfully deleted'
    }
    return JsonResponse(data, status=200)


@login_required
def checkout(request):
    cid = request.GET.get('cid')
    cart = Cart.objects.filter(id=cid).first()
    form = OrderForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.client = request.user
        com.cart = cart
        com.save()
        cart.is_ordered = True
        cart.save()
        messages.success(request, 'Successfully completed!')
        return redirect('.')
    e = request.GET.get('email')
    if e:
        Subscribe.objects.create(email=e)
        return redirect('.')
    ctx = {
        'form': form,
    }
    return render(request, 'checkout.html', ctx)
