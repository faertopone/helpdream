# Generated by Django 4.0.2 on 2022-02-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0057_profile_super_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='creadet_at_time',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата создания для расчета вермени заявки'),
        ),
    ]