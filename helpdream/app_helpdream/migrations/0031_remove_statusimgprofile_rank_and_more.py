# Generated by Django 4.0.2 on 2022-02-26 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0030_rename_creadet_at_writedeam_creadet_at_dream'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statusimgprofile',
            name='rank',
        ),
        migrations.AddField(
            model_name='profile',
            name='max_dream_created',
            field=models.IntegerField(default=5, verbose_name='Сколько создать мечт можно'),
        ),
        migrations.AddField(
            model_name='profile',
            name='max_dream_price',
            field=models.IntegerField(default=15000, verbose_name='Сколько создать мечт можно'),
        ),
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='ранк'),
        ),
    ]