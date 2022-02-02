# Generated by Django 2.2 on 2022-02-01 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_authorbook_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorbook',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='author_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest.AuthorBook', verbose_name='Книги'),
        ),
    ]
