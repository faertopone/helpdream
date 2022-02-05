# Generated by Django 4.0.2 on 2022-02-04 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0009_remove_productreport_product_productreport_count_pay_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='cart_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_shop.profile', verbose_name='Пользователь для этой корзины'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='items',
            field=models.ManyToManyField(blank=True, db_index=True, null=True, to='app_shop.Item', verbose_name='Товары которые добавим в корзину'),
        ),
    ]
