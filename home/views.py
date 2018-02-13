from django.shortcuts import render

from product.models import Product, ProductImage
from django.db.models import Q

import random

# Create your views here.

def home(request):
	products = Product.objects.filter(is_active=True).order_by('?')[:20]
	return render(request, 'home/home.html', locals())