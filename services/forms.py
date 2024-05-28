from django.forms import ModelForm

from services.models import ServicesModel, CartModel, ProductModel, Contact
from services.models import Newsletter


class ServicesForm(ModelForm):

    class Meta:
        model = ServicesModel
        fields = '__all__'


class NewsLetterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
