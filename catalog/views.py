from django.shortcuts import render

def v_home(request):
    return render(request, 'catalog/home.html')

def v_contacts(request):
    return render(request, 'catalog/contacts.html')

