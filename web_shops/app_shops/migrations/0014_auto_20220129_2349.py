# Generated by Django 2.2 on 2022-01-29 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0013_auto_20220129_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotions',
            name='description',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Описание'),
        ),
    ]