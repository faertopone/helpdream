# Generated by Django 2.2 on 2022-01-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0014_auto_20220129_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='description',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Описание'),
        ),
    ]