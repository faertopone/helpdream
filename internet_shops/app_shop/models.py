from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _



#Это добавление к стандартному User новые поля
class Profile(models.Model):
    """
    Модель профиля пользователя.
    """

    def __str__(self):
        return self.user.username

    STATUS_CHOISE = [
        ('Мужской', _('Мужской')),
        ('Женский', _('Женский'))
    ]

    STATUS_PROFILE_CHOISE = [
        ('новичек', _('новичек')),
        ('продвинутый', _('продвинутый')),
        ('эксперт', _('эксперт')),
        ('БОГ покупок', _('БОГ покупок')),
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    gender = models.CharField(max_length=100, choices=STATUS_CHOISE, verbose_name=_('Выберите пол'), db_index=True, default=_('Мужской'))
    avatar = models.ImageField(upload_to='avatars/', verbose_name=_('Фото аватарки'), db_index=True, null=True)
    creadet_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'), db_index=True, null=True)
    phone = models.CharField(max_length=15, verbose_name=_('Телефон'), db_index=True, default='', blank=True)
    balance = models.IntegerField(verbose_name=_('Баланс'), db_index=True, blank=True, default=0)
    status_profile = models.CharField(max_length=100, choices=STATUS_PROFILE_CHOISE, verbose_name=_('Ваш статус профиля'), db_index=True, default=_('новичек'))


    class Meta:
        db_table = 'Profile'
        verbose_name = _('профиль')
        verbose_name_plural = _('профили')



class Shops(models.Model):
    """
    Модель магазинов.
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=30, verbose_name=_('название магазина'), db_index=True, null=True)
    adress = models.CharField(max_length=30, verbose_name=_('адрес'), db_index=True, null=True)
    tel = models.IntegerField(verbose_name=_('телефон'), db_index=True, null=True)


    class Meta:
        db_table = 'Shops'
        verbose_name = _('магазин')
        verbose_name_plural = _('магазины')



class Item(models.Model):
    """
    Модель товаров
    """

    def __str__(self):
        return self.name

    CATEGORY_ITEM_CHOISE = [
        ('еда', _('еда')),
        ('техника', _('техника')),
        ('другое', _('другое')),

    ]


    name = models.CharField(max_length=30, verbose_name=_('название товара'), db_index=True, null=True)
    description = models.TextField(verbose_name=_('описание товара'), db_index=True, null=True, blank=True)
    price = models.FloatField(verbose_name=_('Цена'), db_index=True, default=0)
    amount_item = models.IntegerField(verbose_name=_('количество товара на складе'), db_index=True, default=0)
    count_pay = models.IntegerField(verbose_name=_('количество товара купить'), db_index=True, default=0)
    category_item = models.CharField(max_length=50,  choices=CATEGORY_ITEM_CHOISE, verbose_name=_('Выберите категорию товара'), db_index=True, default=_('другое'))
    shops = models.ManyToManyField(Shops, verbose_name=_('Магазины в которых эти товары'), db_index=True)

    class Meta:
        db_table = 'Item'
        verbose_name = _('товар')
        verbose_name_plural = _('товары')


class ShoppingCart(models.Model):
    """
    Модель корзины.
    """

    def __str__(self):
        return self.cart_user.user

    items = models.ManyToManyField(Item, verbose_name=_('Товары которые добавим в корзину'), db_index=True, blank=True)
    cart_user = models.OneToOneField(Profile, on_delete=models.CASCADE, verbose_name=_('Пользователь для этой корзины'), db_index=True, blank=True)

    class Meta:
        db_table = 'ShoppingCart'
        verbose_name = _('корзина')
        verbose_name_plural = _('корзины')