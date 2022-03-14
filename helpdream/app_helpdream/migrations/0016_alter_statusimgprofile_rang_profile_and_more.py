# Generated by Django 4.0.2 on 2022-02-12 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0015_alter_statusimgprofile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusimgprofile',
            name='rang_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.profile', verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='statusimgprofile',
            name='rank',
            field=models.IntegerField(blank=True, default=0, verbose_name='статус'),
        ),
    ]
