# Generated by Django 5.1.4 on 2025-01-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='text_type',
            field=models.CharField(choices=[('privacy', 'privacy'), ('terms', 'terms'), ('cookies', 'cookies')], max_length=255, verbose_name='Тип текста'),
        ),
    ]
