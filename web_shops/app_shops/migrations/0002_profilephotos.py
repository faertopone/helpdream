# Generated by Django 2.2 on 2022-01-28 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_img', models.ImageField(blank=True, db_index=True, null=True, upload_to='img_blog/', verbose_name='Фото')),
                ('photo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_shops.Profile')),
            ],
            options={
                'verbose_name': 'Фото профиля',
                'verbose_name_plural': 'Фото профилей',
                'db_table': 'Profile_Photo',
            },
        ),
    ]
