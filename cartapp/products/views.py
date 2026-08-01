from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def listproducts(request):
    """_summary_
    Args
    """
    return render(request,'product.html')

def detailproducts(request):
    return render(request,'productdetails.html')