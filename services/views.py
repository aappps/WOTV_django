from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from services.forms import NewsLetterForm
from services.models import ServicesModel, Newsletter


# Create your views here.

class ServicesDetailView(DetailView):
    template_name = "services/details.html"
    model = ServicesModel


class ServicesListView(ListView):
    template_name = "services/all.html"
    model = ServicesModel
    form_class = NewsLetterForm


class ServicesUpdateView(UpdateView):
    form_class = ServicesModel
    template_name = 'create_update_form.html'
    model = ServicesModel
    success_url = reverse_lazy('services-list')


class ServicesDeleteView(DeleteView):
    form_class = ServicesModel
    template_name = 'delete_form.html'
    model = ServicesModel
    success_message = "Deleted successfully"
    success_url = reverse_lazy('services-list')


class ServicesCreateView(CreateView):
    form_class = ServicesModel
    template_name = 'create_update_form.html'
    model = ServicesModel
    success_url = reverse_lazy('services-list')


class SubscribeNewsLetter(CreateView):
    model = Newsletter
    form_class = NewsLetterForm
    template_name = "layout/news.html"

    def form_valid(self, form):
        # Salvează formularul și setează o variabilă care să indice că s-a abonat cu succes
        self.object = form.save()
        subscribed = True
        return self.render_to_response(self.get_context_data(subscribed=subscribed))

