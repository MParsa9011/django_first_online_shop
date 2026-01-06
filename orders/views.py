from django.shortcuts import render

from products.models import Product


def order_create_view(request):
    products = Product.objects.all()
    return render(request, 'orders/order_create.html')
