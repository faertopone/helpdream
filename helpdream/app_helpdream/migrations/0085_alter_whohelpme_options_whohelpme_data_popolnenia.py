# Generated by Django 4.0.2 on 2022-03-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0084_totalboxdream_boxdreamhelp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='whohelpme',
            options={'ordering': ['-data_popolnenia'], 'verbose_name': 'мечта которой помогли', 'verbose_name_plural': 'мечты которым помогли'},
        ),
        migrations.AddField(
            model_name='whohelpme',
            name='data_popolnenia',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
    ]
