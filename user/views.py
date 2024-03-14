from django.contrib.auth.backends import UserModel
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from user.forms import UserForm


# Create your views here.

class UserCreateView(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('user-all')


# READ
class UserListView(ListView):
    model = UserModel
    template_name = 'user/all.html'


# Update
class UserUpdateView(UpdateView):
    model = UserModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('user-all')


class UserDeleteView(DeleteView):
    model = UserModel
    template_name = 'delete_form.html'
    success_url = reverse_lazy('user-all')


class UserDetailView(DetailView):
    model = UserModel
    template_name = 'user/details.html'
