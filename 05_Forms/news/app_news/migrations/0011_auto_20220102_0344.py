# Generated by Django 2.2 on 2022-01-02 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0010_auto_20220102_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mynews',
            name='is_active_news',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Активность новости'),
        ),
    ]