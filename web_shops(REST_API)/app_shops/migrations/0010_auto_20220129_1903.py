# Generated by Django 2.2 on 2022-01-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0009_shops'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='adress',
            field=models.TextField(db_index=True, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='name',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='tel',
            field=models.CharField(db_index=True, max_length=50, null=True, verbose_name='Телефон'),
        ),
    ]