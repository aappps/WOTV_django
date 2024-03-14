

from django.contrib import admin
from django.urls import path
from .views import *

from WOTV import settings
from home.views import home

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('login/', LogoutUserView.as_view(), name='logout'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('password-change/', UserChangePasswordView.as_view(), name='password-change'),

]

