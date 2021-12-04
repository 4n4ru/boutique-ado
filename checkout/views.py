from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's notthing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K0Vw9FLDSYHQzon8hNpMxbU6l5UPgCceKhOazVFD2jELWIoPLa8GKPiUw1rgxeO6j7Jttbh2hbHBG4XpMPvacuK00Z07bJgC9',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
