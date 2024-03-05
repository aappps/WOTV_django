from django.shortcuts import render
from django.views.generic import ListView

from products.models import ProductsModel


# Create your views here.

def home(request):
    return render(request, template_name='home/home.html', context={})


class HomeView(ListView):
    template_name = 'home/home.html'
    model = ProductsModel


