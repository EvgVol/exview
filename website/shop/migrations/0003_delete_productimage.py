# Generated by Django 4.2.4 on 2023-09-08 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_productimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]