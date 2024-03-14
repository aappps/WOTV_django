from django.contrib.auth.forms import UserModel
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'
