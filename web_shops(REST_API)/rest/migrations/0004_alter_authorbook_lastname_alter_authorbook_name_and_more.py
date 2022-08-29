# Generated by Django 4.0.2 on 2022-02-03 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0003_auto_20220201_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorbook',
            name='lastname',
            field=models.CharField(max_length=40, null=True, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='authorbook',
            name='name',
            field=models.CharField(max_length=40, null=True, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='authorbook',
            name='yearofbirth',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest.authorbook', verbose_name='Автор книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(null=True, verbose_name='международный стандартный книжный номер'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=40, null=True, verbose_name='Название книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='numberofpages',
            field=models.IntegerField(null=True, verbose_name='Количество страниц'),
        ),
        migrations.AlterField(
            model_name='book',
            name='yearofissue',
            field=models.DateField(null=True, verbose_name='Год выпуска'),
        ),
    ]