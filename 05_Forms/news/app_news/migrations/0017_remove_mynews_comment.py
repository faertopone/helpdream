# Generated by Django 2.2 on 2022-01-02 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0016_auto_20220102_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mynews',
            name='comment',
        ),
    ]