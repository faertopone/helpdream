# Generated by Django 2.2 on 2022-01-15 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, db_index=True, max_length=40, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateTimeField(db_index=True, verbose_name='дата рождения'),
        ),
    ]
