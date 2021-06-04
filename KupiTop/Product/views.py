from django.shortcuts import render
from .models import Product

def index(request):
    discounts = Product.objects.filter(discount=True)
    products = Product.objects.all()
    if len(discounts) > 0:
        return render(request, 'index.html', {'discount_product': discounts[0],
                                              'discount_products': discounts[1:],
                                              'discount': True,
                                              'products': products})
    else:
        return render(request, 'index.html', {'products': products, 'discount': False})