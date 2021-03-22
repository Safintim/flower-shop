from cart.models import Cart


def cart(request):
    price_total = 0
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        price_total = cart.price_total

    return {
        'cart_price_total': price_total
    }
