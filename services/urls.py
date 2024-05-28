"""
URL configuration for WOTV project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path

from home.views import HomeView

from services.views import ServicesListView, ServicesDeleteView, ServicesUpdateView, \
    ServicesCreateView, SubscribeNewsLetter, ServicesSecondDetailView, ProductDetailView, cart_view, add_to_cart, \
    contact_view, success_view

urlpatterns = [
    path('', ServicesListView.as_view(), name='services-list'),
    path('news/', SubscribeNewsLetter.as_view(), name='subscribe-newsletter'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='services-details'),
    path('details/<int:pk>/', ServicesSecondDetailView.as_view(), name='services-details-page'),
    path('update/<int:pk>/', ServicesUpdateView.as_view(), name='services-edit'),
    path('delete/<int:pk>/', ServicesDeleteView.as_view(), name='services-delete'),
    path('add/', ServicesCreateView.as_view(), name='add-services'),
    path('cart/', cart_view, name='cart-view'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('contact/<int:pk>/', contact_view, name='services-details-page'),
    path('contact/success/', success_view, name='contact_success'),

]
