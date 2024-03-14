from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name', 'last_name']
        model = User

    def save(self, commit=True):
        self.instance.is_active = False
        return super().save(commit)
