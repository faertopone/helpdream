# Generated by Django 2.2 on 2022-01-15 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_employment', '0002_summary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='summary',
            options={'permissions': (('Can add', 'Может создавать'), ('Can change', 'Может редактировать'), ('Can delete', 'Может удалять'), ('Can_view', 'Может просматривать')), 'verbose_name': 'Резюме', 'verbose_name_plural': 'Все резюме'},
        ),
    ]
