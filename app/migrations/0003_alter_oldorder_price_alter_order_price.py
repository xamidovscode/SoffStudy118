# Generated by Django 5.2 on 2025-04-07 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_oldorder_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oldorder',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
