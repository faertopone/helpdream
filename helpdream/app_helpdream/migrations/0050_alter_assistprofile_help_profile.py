# Generated by Django 4.0.2 on 2022-02-26 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0049_alter_writedeam_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistprofile',
            name='help_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.whohelpme', verbose_name='Какая мечта'),
        ),
    ]
