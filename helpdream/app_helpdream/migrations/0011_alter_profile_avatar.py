# Generated by Django 4.0.2 on 2022-02-12 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0010_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, db_index=True, null=True, upload_to='avatars/', verbose_name='Выберите файл'),
        ),
    ]
