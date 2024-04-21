from django.forms import ModelForm

from services.models import ServicesModel, CartModel
from services.models import Newsletter


class ServicesForm(ModelForm):

    class Meta:
        model = ServicesModel
        fields = '__all__'


class NewsLetterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'


