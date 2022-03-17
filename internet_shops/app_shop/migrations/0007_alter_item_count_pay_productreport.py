# Generated by Django 4.0.2 on 2022-02-04 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0006_profile_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='count_pay',
            field=models.IntegerField(db_index=True, default=0, verbose_name='количество товара купили'),
        ),
        migrations.CreateModel(
            name='ProductReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('product', models.ManyToManyField(blank=True, db_index=True, null=True, to='app_shop.Item', verbose_name='Проданные товары')),
            ],
        ),
    ]
