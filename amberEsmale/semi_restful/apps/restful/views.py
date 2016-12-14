from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def direct(request):
    return redirect('/products')

def index(request):
    context = {
        'all_products' : Product.objects.all()
    }
    return render(request, "restful/index.html", context)

def show(request, id):
    context = {
        'product' : Product.objects.get(id = id)
    }
    return render(request, "restful/show.html", context)

def new(request):
    return render(request, "restful/new.html")

def create(request):
    Product.objects.create(name = request.POST['name'], description = request.POST['description'], price = request.POST['price'])
    return redirect('/products')

def edit(request, id):
    context = {
        'product' : Product.objects.get(id = id)
    }
    return render(request, "restful/edit.html", context)

def update(request, id):
    product = Product.objects.get(id = id)
    product.name = request.POST['name']
    product.description = request.POST['description']
    product.price = request.POST['price']
    product.save()
    return redirect('/products')

def destroy(request, id):
    Product.objects.filter(id = id).delete()
    return redirect('/products')
