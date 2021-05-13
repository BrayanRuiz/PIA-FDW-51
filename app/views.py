from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def productos(request):
    return render(request, 'productos.html')
def contacto(request):
    return render(request, 'contacto.html')