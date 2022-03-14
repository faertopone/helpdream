# Generated by Django 4.0.2 on 2022-02-09 01:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], db_index=True, default='Мужской', max_length=100, verbose_name='Выберите пол')),
                ('avatar', models.ImageField(db_index=True, null=True, upload_to='avatars/', verbose_name='Выберите файл')),
                ('creadet_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата создания')),
                ('phone', models.CharField(blank=True, db_index=True, default='', max_length=15, verbose_name='Телефон')),
                ('my_balance', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Баланс')),
                ('status', models.CharField(default='новичек', max_length=40, verbose_name='статус')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='возраст')),
                ('help_balanced', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='на сколько помогли')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'профиль',
                'verbose_name_plural': 'профили',
                'db_table': 'Profile',
            },
        ),
    ]
