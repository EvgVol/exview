# Generated by Django 4.2.1 on 2023-08-16 12:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Текст')),
                ('slug', models.SlugField(unique_for_date='publish', verbose_name='Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('IN', 'Недействующая'), ('CR', 'Действующая')], default='IN', max_length=2, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Политика конфиденциальности',
                'verbose_name_plural': 'Политика конфиденциальности',
                'ordering': ['-publish'],
                'indexes': [models.Index(fields=['-publish'], name='core_policy_publish_7abe31_idx')],
            },
        ),
    ]
