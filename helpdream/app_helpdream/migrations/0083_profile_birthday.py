# Generated by Django 4.0.2 on 2022-03-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0082_profile_all_info_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
    ]