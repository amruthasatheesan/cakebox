# Generated by Django 4.1.3 on 2023-05-04 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_cakes_image_alter_orders_expected_deliverydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='matter',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='cakes',
            name='image',
            field=models.ImageField(default=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='expected_deliverydate',
            field=models.DateField(default=datetime.date(2023, 5, 6)),
        ),
    ]