from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView, PasswordResetView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from authentication.forms import CreateUserForm


# Create your views here.

class UserActions(TemplateView):
    template_name = 'authentication/user_actions.html'


class LoginUserView(LoginView):
    template_name = "authentication/form.html"
    success_url = reverse_lazy('')
    redirect_authenticated_user = True


class UserChangePasswordView(PasswordChangeView):
    template_name = "authentication/form.html"
    success_url = reverse_lazy('')  # login


class CreateUserView(CreateView):
    template_name = "authentication/form.html"
    success_url = reverse_lazy('')
    form_class = CreateUserForm


class LogoutUserView(LogoutView):
    success_url = reverse_lazy('')  # logaout


class ResetUserPassword(PasswordResetView):
    success_url = reverse_lazy('')
