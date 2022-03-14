# Generated by Django 4.0.2 on 2022-03-01 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_helpdream', '0070_rename_text_comments_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(db_index=True, max_length=30, null=True, verbose_name='Какой банк')),
                ('amount', models.IntegerField(db_index=True, null=True, verbose_name='Сумма денег')),
                ('dt_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата совершении оплаты')),
                ('other_info', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Еще какая то информация')),
                ('whom', models.ForeignKey(blank=True, default='пусто', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователя кому перечислил денег')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='payment_history',
            field=models.ManyToManyField(blank=True, db_index=True, to='app_helpdream.PaymentHistory', verbose_name='Модель историй оплаты'),
        ),
    ]
