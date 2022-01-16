# Generated by Django 2.2 on 2022-01-04 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0037_remove_mynews_all_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycomments',
            name='old_description',
            field=models.TextField(db_index=True, default='', verbose_name='Хранения комментария после удаления'),
        ),
        migrations.AddField(
            model_name='mycomments',
            name='status_comment',
            field=models.BooleanField(choices=[(True, 'Удалено администратором'), (False, 'Комментарий норм')], db_index=True, default=False, verbose_name='статус'),
        ),
    ]