# Generated by Django 4.0.2 on 2022-02-27 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0059_remove_whohelpme_where_dream_writedeam_where_dream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writedeam',
            name='where_dream',
            field=models.ManyToManyField(blank=True, db_index=True, null=True, to='app_helpdream.WhoHelpMe', verbose_name='Профиль кто помог этой мечте'),
        ),
    ]
