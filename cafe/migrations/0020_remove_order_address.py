# Generated by Django 4.0.4 on 2022-05-15 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0019_order_studentid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
    ]
