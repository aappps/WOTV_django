from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from products.models import ProductsModel


# Create your views here.

class ProductsDetailView(DetailView):
    template_name = "products/details.html"
    model = ProductsModel


class ProductsListView(ListView):
    template_name = "products/all.html"
    model = ProductsModel


class ProductsUpdateView(UpdateView):
    form_class = ProductsModel
    template_name = 'create_update_form.html'
    model = ProductsModel
    success_url = reverse_lazy('products-list')


class ProductsDeleteView(DeleteView):
    form_class = ProductsModel
    template_name = 'delete_form.html'
    model = ProductsModel
    success_message = "Deleted successfully"
    success_url = reverse_lazy('products-list')


class ProductsCreateView(CreateView):
    form_class = ProductsModel
    template_name = 'create_update_form.html'
    model = ProductsModel
    success_url = reverse_lazy('products-list')
