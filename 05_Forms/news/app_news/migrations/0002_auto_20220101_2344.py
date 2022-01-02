# Generated by Django 2.2 on 2022-01-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, verbose_name='mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(db_index=True, default='', max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='second_name',
            field=models.CharField(db_index=True, default='', max_length=20, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Имя'),
        ),
    ]