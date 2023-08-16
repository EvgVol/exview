# Generated by Django 4.2.1 on 2023-08-16 11:37

import account.validators
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует!'}, help_text='Обязательно для заполнения. От 3 до 32 букв.', max_length=32, unique=True, validators=[account.validators.validate_username], verbose_name='Уникальный юзернейм')),
                ('first_name', models.CharField(blank=True, help_text='Обязательно для заполнения. Максимум 32 букв.', max_length=32, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Обязательно для заполнения. Максимум 32 букв.', max_length=32, null=True, verbose_name='Фамилия')),
                ('email', models.EmailField(help_text='Обязательно для заполнения. Максимум 256 букв.', max_length=256, unique=True, verbose_name='Электронная почта')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('avatar', models.ImageField(blank=True, help_text='Наличие аватара увеличивает к вам доверие', null=True, upload_to='accounts/images/', verbose_name='Изображение')),
                ('phone_number', models.CharField(blank=True, help_text='Укажите номер телефона для связи', max_length=12, validators=[django.core.validators.RegexValidator(message='Проверьте корректно ли указан номер телефона', regex='^(\\+7|8)\\d{10}$')], verbose_name='Номер телефона')),
                ('about_me', models.TextField(blank=True, help_text='Укажите информацию о себе', verbose_name='О себе')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('username',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписки',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='account.Contact', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['-created'], name='account_con_created_8bdae6_idx'),
        ),
        migrations.AddConstraint(
            model_name='contact',
            constraint=models.UniqueConstraint(fields=('user_from', 'user_to'), name='unique_follow'),
        ),
        migrations.AddConstraint(
            model_name='contact',
            constraint=models.CheckConstraint(check=models.Q(('user_to', models.F('user_from')), _negated=True), name='no_self_follow'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username', 'email'), name='unique_username_email'),
        ),
    ]
