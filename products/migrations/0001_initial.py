# Generated by Django 5.0.2 on 2024-03-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('beneath_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=5000)),
                ('image_field', models.ImageField(upload_to='all.html')),
            ],
        ),
    ]
