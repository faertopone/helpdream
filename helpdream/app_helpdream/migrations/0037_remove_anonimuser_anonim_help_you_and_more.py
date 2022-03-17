# Generated by Django 4.0.2 on 2022-02-26 20:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0036_profile_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anonimuser',
            name='anonim_help_you',
        ),
        migrations.RemoveField(
            model_name='whohelpme',
            name='who_help_me',
        ),
        migrations.AddField(
            model_name='whohelpme',
            name='who_avatar',
            field=models.CharField(blank=True, default='img_status/zvezda0.png', max_length=100, verbose_name='Ссылка на аву'),
        ),
        migrations.AddField(
            model_name='whohelpme',
            name='who_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='whohelpme',
            name='who_price',
            field=models.IntegerField(blank=True, db_index=True, default=0, verbose_name='на сколько помогли '),
        ),
        migrations.AddField(
            model_name='whohelpme',
            name='who_rank',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='ранк'),
        ),
        migrations.AlterField(
            model_name='whohelpme',
            name='who_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.profile', verbose_name='Кто мне помог'),
        ),
    ]
