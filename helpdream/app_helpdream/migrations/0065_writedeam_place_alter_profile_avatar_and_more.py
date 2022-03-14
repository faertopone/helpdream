# Generated by Django 4.0.2 on 2022-02-27 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0064_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='writedeam',
            name='place',
            field=models.IntegerField(blank=True, null=True, verbose_name='слот для расчета позиции '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, db_index=True, default='avatars/user-avatar.svg', upload_to='avatars/', verbose_name='Аватарка'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, db_index=True, default='img_status/zvezda0.png', upload_to='img_status/', verbose_name='ранг'),
        ),
    ]
