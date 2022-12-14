# Generated by Django 4.0.2 on 2022-03-09 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0085_alter_whohelpme_options_whohelpme_data_popolnenia'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryBoxDream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_win', models.IntegerField(db_index=True, default=1, verbose_name='номер розыгрыша')),
                ('data_win_box', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата розыгрыша')),
            ],
            options={
                'db_table': 'HistoryBoxDream',
                'ordering': ['data_win_box'],
            },
        ),
        migrations.CreateModel(
            name='WinDream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_help_box', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Сколько денег мечта получила через BOXDREAM')),
                ('who_dream_box', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.writedeam', verbose_name='Какой мечте помогли')),
            ],
        ),
        migrations.AddField(
            model_name='totalboxdream',
            name='count_win_box',
            field=models.IntegerField(db_index=True, default=1, verbose_name='Какой по счету розыгрыш'),
        ),
        migrations.DeleteModel(
            name='BoxDreamHelp',
        ),
        migrations.AddField(
            model_name='historyboxdream',
            name='win_dream',
            field=models.ManyToManyField(db_index=True, to='app_helpdream.WinDream', verbose_name='Мечта с параметрами кто выграл'),
        ),
    ]
