# Generated by Django 4.0.2 on 2022-02-12 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0005_remove_profile_status_statusimgprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statusimgprofile',
            options={'verbose_name': 'статус профиля', 'verbose_name_plural': 'статусы профиля'},
        ),
        migrations.AlterModelTable(
            name='statusimgprofile',
            table='StatusImgProfile',
        ),
    ]
