# Generated by Django 4.0.2 on 2022-02-09 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, db_index=True, default='', max_length=40, verbose_name='Телефон'),
        ),
    ]
