from django import template
from apps.cart.models import Cart, Wishlist

register = template.Library()


@register.simple_tag(takes_context=True)
def get_cart(context):
    request = context['request']
    user = request.user
    try:
        cart = Cart.objects.get(user=user, is_ordered=False)
    except:
        cart = None
    return cart
