from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ServicesModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    beneath_name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=5000, null=False)
    image_field = models.ImageField(upload_to='media/', null=False)

    def __str__(self):
        return f"{self.name} - {self.description} - {self.beneath_name} - {self.image_field}"


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.ImageField(upload_to='dyi/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.price} "


class CartModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.quantity} - {self.total}"


class Newsletter(models.Model):
    email = models.EmailField(null=False)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    message = models.TextField(max_length=5000, null=False)

    def __str__(self):
        return f"{self.name}"
