# Generated by Django 2.2 on 2022-01-15 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_employment', '0007_auto_20220116_0001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'permissions': (('publish', 'Может публиковать'),), 'verbose_name': 'вакансия', 'verbose_name_plural': 'вакансии'},
        ),
    ]