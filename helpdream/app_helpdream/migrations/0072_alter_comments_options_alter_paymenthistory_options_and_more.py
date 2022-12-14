# Generated by Django 4.0.2 on 2022-03-01 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_helpdream', '0071_paymenthistory_profile_payment_history'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Инфо о комменте', 'verbose_name_plural': 'Информация о коментариях'},
        ),
        migrations.AlterModelOptions(
            name='paymenthistory',
            options={'verbose_name': 'История операции', 'verbose_name_plural': 'История операций'},
        ),
        migrations.AddField(
            model_name='writedeam',
            name='comments',
            field=models.ManyToManyField(blank=True, db_index=True, to='app_helpdream.Comments', verbose_name='Модели комментария'),
        ),
        migrations.AlterModelTable(
            name='comments',
            table='Comments',
        ),
        migrations.AlterModelTable(
            name='paymenthistory',
            table='PaymentHistory',
        ),
    ]
