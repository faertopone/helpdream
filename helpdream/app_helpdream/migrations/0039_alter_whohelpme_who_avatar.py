# Generated by Django 4.0.2 on 2022-02-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0038_alter_whohelpme_options_alter_whohelpme_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whohelpme',
            name='who_avatar',
            field=models.CharField(blank=True, default='avatars/user-avatar.svg', max_length=100, verbose_name='Ссылка на аву'),
        ),
    ]
