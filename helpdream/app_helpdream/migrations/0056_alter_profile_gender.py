# Generated by Django 4.0.2 on 2022-02-26 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0055_alter_profile_img_alter_profile_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], db_index=True, default='Мужской', max_length=100, verbose_name='Выберите пол'),
        ),
    ]