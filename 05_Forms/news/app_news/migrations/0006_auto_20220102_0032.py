# Generated by Django 2.2 on 2022-01-01 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_auto_20220102_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active_user',
            field=models.BooleanField(db_index=True, default=False, verbose_name='актив'),
        ),
        migrations.AlterField(
            model_name='user',
            name='second_name',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Отчество'),
        ),
    ]