from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from products.models import ProductsModel


# Create your views here.

def home(request):
    return render(request, template_name='home/home.html', context={})


class HomeView(ListView):
    template_name = 'home/home.html'
    model = ProductsModel


class PortofolioView(TemplateView):
    template_name = "home/portofolio.html"


class WotvView(TemplateView):
    template_name = "home/wotv.html"

