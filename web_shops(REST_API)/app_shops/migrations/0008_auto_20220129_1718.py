# Generated by Django 2.2 on 2022-01-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0007_profile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Баланс'),
        ),
    ]