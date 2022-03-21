# Generated by Django 4.0.2 on 2022-02-26 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0045_alter_whohelpme_who_avatar_alter_whohelpme_who_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssistProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assist_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.profile', verbose_name='Вспомогательная таблица')),
                ('help_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.whohelpme', verbose_name='Какая мечта')),
            ],
            options={
                'verbose_name': 'связь с профиль - мечта',
                'verbose_name_plural': 'связи профилей с мечтой',
                'db_table': 'AssistProfile',
            },
        ),
    ]