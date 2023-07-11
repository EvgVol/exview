# Generated by Django 4.2.1 on 2023-07-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(help_text='Enter a description', max_length=600, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='course',
            name='overview',
            field=models.CharField(max_length=50, verbose_name='overview'),
        ),
    ]
