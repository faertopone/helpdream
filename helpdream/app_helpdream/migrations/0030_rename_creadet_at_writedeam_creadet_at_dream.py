# Generated by Django 4.0.2 on 2022-02-25 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0029_writedeam_updated_dream'),
    ]

    operations = [
        migrations.RenameField(
            model_name='writedeam',
            old_name='creadet_at',
            new_name='creadet_at_dream',
        ),
    ]
