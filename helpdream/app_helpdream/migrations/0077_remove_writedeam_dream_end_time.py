# Generated by Django 4.0.2 on 2022-03-03 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0076_writedeam_dream_end_time_alter_profile_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writedeam',
            name='dream_end_time',
        ),
    ]