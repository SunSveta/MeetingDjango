from django.shortcuts import render
from catalog.models import Product, Category

def v_home(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)

def v_contacts(request):
    return render(request, 'catalog/contacts.html')

def prod_card(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/prod_card.html', context)

