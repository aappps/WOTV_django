from django.forms import ModelForm

from products.models import ProductsModel


class ProductsForm(ModelForm):

    class Meta:
        model = ProductsModel
        fields = '__all__'