# Generated by Django 2.2 on 2022-01-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0002_profilephotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='creadet_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата создания'),
        ),
    ]
