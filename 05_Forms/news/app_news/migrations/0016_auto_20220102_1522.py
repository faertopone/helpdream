# Generated by Django 2.2 on 2022-01-02 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0015_auto_20220102_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycomments',
            name='comment_news',
        ),
        migrations.AddField(
            model_name='mynews',
            name='comment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_news.MyComments', verbose_name='Коментарии'),
        ),
    ]