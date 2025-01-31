# Generated by Django 4.0.4 on 2022-05-07 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0006_alter_customer_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/images/carousel/')),
            ],
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.IntegerField(),
        ),
    ]
