# Generated by Django 2.2 on 2022-01-23 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_blog_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(db_index=True, default='Аноним', max_length=100, verbose_name='Автор'),
        ),
    ]
