# Generated by Django 4.0.2 on 2022-03-15 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0093_alter_comments_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='content',
        ),
    ]
