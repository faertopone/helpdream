# Generated by Django 4.0.2 on 2022-02-12 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0003_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('rang0', 'Ранг 0'), ('rang1', 'Ранг 1'), ('rang2', 'Ранг 2'), ('rang3', 'Ранг 3'), ('rang4', 'Ранг 4'), ('rang5', 'Ранг 5')], default='rang0', max_length=40, verbose_name='статус'),
        ),
    ]