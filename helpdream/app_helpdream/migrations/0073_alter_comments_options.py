# Generated by Django 4.0.2 on 2022-03-01 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0072_alter_comments_options_alter_paymenthistory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-data_created'], 'verbose_name': 'Инфо о комменте', 'verbose_name_plural': 'Информация о коментариях'},
        ),
    ]
