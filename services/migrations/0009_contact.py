# Generated by Django 5.0.2 on 2024-05-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_productmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=5000)),
            ],
        ),
    ]