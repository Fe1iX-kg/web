from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def address(request):
    return render(request, 'address.html')

def support(request):
    return render(request, 'support.html')

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    context = {'company_name': 'Моя Компания', 'year': 2025}
    return render(request, 'about.html', context)