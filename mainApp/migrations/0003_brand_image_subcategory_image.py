# Generated by Django 5.0.1 on 2024-04-19 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_product_finalprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
    ]