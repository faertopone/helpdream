# Generated by Django 4.0.2 on 2022-03-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0087_writedeam_number_for_draw'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historyboxdream',
            options={'ordering': ['-data_win_box']},
        ),
        migrations.AlterField(
            model_name='historyboxdream',
            name='win_dream',
            field=models.ManyToManyField(blank=True, db_index=True, to='app_helpdream.WinDream', verbose_name='Мечта с параметрами кто выграл'),
        ),
    ]
