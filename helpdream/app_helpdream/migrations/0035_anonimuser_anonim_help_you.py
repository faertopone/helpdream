# Generated by Django 4.0.2 on 2022-02-26 17:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_helpdream', '0034_rename_anoninuser_anonimuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anonimuser',
            name='anonim_help_you',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Кому аноним помог'),
        ),
    ]
