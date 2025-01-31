# Generated by Django 4.0.4 on 2022-05-12 13:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0009_alter_carousel_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='message',
            field=models.CharField(default='Banner Size must be 700X350 ', max_length=200),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.items')),
            ],
        ),
    ]
