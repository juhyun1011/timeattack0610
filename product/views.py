from django.http import HttpResponse
from django.shortcuts import render
from .models import Product



def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')

    elif request.method == 'POST':
        category = request.POST.get("category")
        print(category)
        current_products = Product.objects.filter(category_id=category)
        print(current_products)
        return render(request, 'home.html', {"current_products": current_products})