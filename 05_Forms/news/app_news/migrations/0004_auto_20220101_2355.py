# Generated by Django 2.2 on 2022-01-01 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_user_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['created_at']},
        ),
    ]
