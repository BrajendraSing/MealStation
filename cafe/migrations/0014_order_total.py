# Generated by Django 4.0.4 on 2022-05-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0013_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
