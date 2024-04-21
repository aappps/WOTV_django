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
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)


class CartModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.product} - {self.quantity} - {self.total}"


class Newsletter(models.Model):
    email = models.EmailField(null=False)
