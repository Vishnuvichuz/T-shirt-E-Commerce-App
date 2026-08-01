from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('productlist',views.listproducts,name='listproducts'),
    path('productdetails',views.detailproducts,name='productdetails')

]