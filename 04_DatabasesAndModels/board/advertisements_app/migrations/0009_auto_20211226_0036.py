# Generated by Django 2.2 on 2021-12-25 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements_app', '0008_auto_20211226_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='type',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
