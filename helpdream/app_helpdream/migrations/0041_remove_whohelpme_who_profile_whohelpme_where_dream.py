# Generated by Django 4.0.2 on 2022-02-26 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0040_alter_whohelpme_who_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whohelpme',
            name='who_profile',
        ),
        migrations.AddField(
            model_name='whohelpme',
            name='where_dream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.writedeam', verbose_name='Какая мечта'),
        ),
    ]
