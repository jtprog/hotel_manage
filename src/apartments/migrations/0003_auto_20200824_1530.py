# Generated by Django 3.1 on 2020-08-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_remove_apartment_floor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]