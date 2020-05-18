from django.shortcuts import render, reverse, redirect

# Create your views here.

def view_cart(request):
    """Renders everything in the cart"""
    return render(request, 'cart.html')



def add_to_cart(request, id):
    """Add quantity of the specified product of the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """Adjust the quantity of a specified product by a specified amount"""
    quantity = int(request.session.POST('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else: 
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

