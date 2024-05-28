from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required

from services.forms import NewsLetterForm, ContactForm
from services.models import ServicesModel, Newsletter, CartModel, ProductModel
from django.contrib.auth.models import User


class ServicesSecondDetailView(DetailView):
    template_name = "services/details_page.html"
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def form_valid(self, form):
        self.object = form.save()
        subscribed = True
        return self.render_to_response(self.get_context_data(subscribed=subscribed))


@login_required
def cart_view(request):
    user_cart_items = CartModel.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in user_cart_items)
    return render(request, 'services/cart.html', {'user_cart_items': user_cart_items, 'total_price': total_price})



def add_to_cart(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)

    if request.user.is_authenticated:
        # Verifică dacă produsul există deja în coș
        existing_cart_item = CartModel.objects.filter(user=request.user, product=product).first()

        if existing_cart_item:
            # Dacă produsul există, actualizează cantitatea
            existing_cart_item.quantity += 1
            existing_cart_item.save()
        else:
            # Dacă produsul nu există, creează o nouă înregistrare în coș
            new_cart_item = CartModel(user=request.user, product=product, quantity=1)
            new_cart_item.save()

        return redirect('cart-view')
    else:
        return redirect('login')


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'services/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products_section1'] = ProductModel.objects.filter(price__lte=10)
        context['products_section2'] = ProductModel.objects.filter(price__gt=10)
        return context


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartModel, id=item_id)
    cart_item.delete()
    return redirect('cart-view')


def contact_view(request, pk):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'services/details_page.html')


def success_view(request):
    success_message = "Thank you! We received your message!"

    return render(request, 'services/contact_success.html', {'success_message': success_message})
