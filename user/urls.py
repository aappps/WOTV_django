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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from home.views import home
from products.views import ProductsListView, ProductsDetailView, ProductsUpdateView, ProductsDeleteView, \
    ProductsCreateView
from user.views import UserDetailView, UserListView, UserUpdateView, UserDeleteView, UserCreateView

urlpatterns = [
    path('', UserListView.as_view(), name='user-all'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-details'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-edit'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('add/<int:pk>/', UserCreateView.as_view(), name='add-user'),


]
