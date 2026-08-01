
from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    return render(request,'index.html')

def listproducts(request):

    productlist=Product.objects.all()
    context={'products':productlist}

    return render(request,'product.html')

def detailproducts(request):
    product=Product.objects.get(pk=pk)
    context={'products':product}
    return render(request,'productdetails.html',context)