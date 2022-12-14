# Generated by Django 4.0.2 on 2022-02-27 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0063_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, db_index=True, default='ALL_DATA_FILES/avatars/user-avatar.svg', upload_to='avatars/', verbose_name='Выберите файл'),
        ),
    ]
