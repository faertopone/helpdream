# Generated by Django 4.0.2 on 2022-02-28 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0067_whohelpme_messages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whohelpme',
            name='help_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.profile', verbose_name='Профиль кто помог'),
        ),
        migrations.AlterField(
            model_name='whohelpme',
            name='messages',
            field=models.TextField(blank=True, db_index=True, null=True, verbose_name='Сообщение при донате'),
        ),
    ]
