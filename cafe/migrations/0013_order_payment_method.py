# Generated by Django 4.0.4 on 2022-05-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0012_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
