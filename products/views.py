from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()
    return HttpResponse('hello world')