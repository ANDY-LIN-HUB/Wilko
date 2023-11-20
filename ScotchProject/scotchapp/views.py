from django.shortcuts import render, redirect
from .models import MenuItem

def index(request):
    context = {}
    for t in MenuItem.TYPE:
        context[f'menu_{t[0]}'] = MenuItem.objects.filter(type__exact=t[0])
    
    cart = request.session.get('cart', {})
    cart_items = MenuItem.objects.filter(id__in=cart.keys())
    for item in cart_items:
        item.quantity = cart[str(item.id)]
    context['cart_items'] = cart_items

    return render(request, 'scotchapp/index.html', context)

def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    if item_id in cart:
        cart[item_id] += 1
    else:
        cart[item_id] = 1
    request.session['cart'] = cart
    request.session.save()  # Save the session
    return redirect('index')


def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    item_id = str(item_id)  # Convert item_id to string
    if item_id in cart:
        if cart[item_id] > 1:
            cart[item_id] -= 1
        else:
            del cart[item_id]
    request.session['cart'] = cart
    request.session.save()
    return redirect('index')