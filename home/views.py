from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from services.models import ServicesModel


# Create your views here.

def home(request):
    return render(request, template_name='home/home.html', context={})


class HomeView(ListView):
    template_name = 'home/home.html'
    model = ServicesModel


class PortfolioView(TemplateView):
    template_name = "home/portfolio.html"


class WotvView(TemplateView):
    template_name = "home/wotv.html"

