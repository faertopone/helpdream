# Generated by Django 4.0.2 on 2022-02-23 19:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_helpdream', '0018_whohelpme_mehelpyou'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mehelpyou',
            name='me_help_you',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Кому я помог'),
        ),
        migrations.AlterField(
            model_name='whohelpme',
            name='who_help_me',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Кто мне помог'),
        ),
    ]