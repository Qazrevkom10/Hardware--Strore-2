from django.shortcuts import render, get_object_or_404

from .forms import SearchForm
from .models import Product


def store(request):
    context = {}
    return render(request, 'store/store.html', context)
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)



def search(request):
    form = SearchForm(request.GET)
    products = []

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        products = Product.objects.filter(name__icontains=search_query)

    context = {'form': form, 'products': products}
    return render(request, 'store/search.html', context)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler403(request, exception):
    return render(request, '403.html', status=403)

def handler400(request, exception):
    return render(request, '400.html', status=400)

def handler500(request):
    return render(request, '500.html', status=500)
