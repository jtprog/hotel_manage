# Generated by Django 3.1 on 2020-08-24 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20200824_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='status',
        ),
    ]
