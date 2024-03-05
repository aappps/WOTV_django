from django.db import models


# Create your models here.
class ProductsModel(models.Model):
    name = models.CharField(max_length=100, null=False)
    beneath_name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=5000, null=False)
    image_field = models.ImageField(upload_to='all.html')

    def __str__(self):
        return f"{self.name} - {self.description} - {self.beneath_name} - {self.image_field}"


