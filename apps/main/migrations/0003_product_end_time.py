# Generated by Django 5.1.4 on 2025-01-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='Конец'),
        ),
    ]
