# Generated by Django 5.0.1 on 2024-04-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_checkout_checkoutproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproducts',
            name='qty',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='checkoutproducts',
            name='total',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
