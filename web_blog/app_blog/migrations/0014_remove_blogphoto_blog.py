# Generated by Django 2.2 on 2022-01-24 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0013_auto_20220124_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogphoto',
            name='blog',
        ),
    ]
