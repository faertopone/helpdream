# Generated by Django 2.2 on 2022-01-24 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0016_auto_20220124_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogphoto',
            name='blog',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='app_blog.Blog'),
        ),
    ]
