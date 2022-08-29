from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


#Это добавление к стандартному User новые поля
class Profile(models.Model):
    def __str__(self):
        return self.user.username

    STATUS_CHOISE = [
        ('Мужской', _('Мужской')),
        ('Женский', _('Женский'))
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    gender = models.CharField(max_length=100, choices=STATUS_CHOISE, verbose_name=_('Выберите пол'), db_index=True, default=_('Мужской'))
    avatar = models.ImageField(upload_to='avatars/', verbose_name=_('Выберите файл'), db_index=True, null=True)
    creadet_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'), db_index=True, null=True)
    phone = models.CharField(max_length=15, verbose_name=_('Телефон'), db_index=True, default='', blank=True)
    balance = models.IntegerField(verbose_name=_('Баланс'), db_index=True, blank=True, default=0)


    class Meta:
        db_table = 'Profile'
        verbose_name = _('профиль')
        verbose_name_plural = _('профили')

# тут хранятсья фото пользователя
class ProfilePhotos(models.Model):

    def __str__(self):
        name = self.photo.user.username
        return name

    photo = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, verbose_name=_('Пользователь фотки'))
    photo_img = models.ImageField(upload_to='img_blog/', verbose_name=_('Фото'), db_index=True, null=True, blank=True)

    class Meta:
        db_table = 'Profile_Photo'
        verbose_name = _('Фото профиля')
        verbose_name_plural = _('Фото профилей')

class Shops(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50, verbose_name=_('Название'), db_index=True, null=True)
    adress = models.TextField(verbose_name=_('Адрес'), db_index=True, null=True)
    tel = models.CharField(max_length=50, verbose_name=_('Телефон'), db_index=True, null=True)

    class Meta:
        db_table = 'Shops'
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазины')

class PurchaseHistory(models.Model):

    def __str__(self):
        return self.name_product

    user_history = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, verbose_name=_('История покупок пользователя'))
    name_product = models.CharField(max_length=50, verbose_name=_('Название товара'), db_index=True, null=True)
    price = models.IntegerField(verbose_name=_('Цена'), db_index=True, null=True)
    creadet_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата покупки'), db_index=True, null=True)
    count_product = models.IntegerField(verbose_name=_('Количество'), db_index=True, null=True,)

    class Meta:
        db_table = 'PurchaseHistory'
        verbose_name = _('История с товара')
        verbose_name_plural = _('истории с товарами')


class Promotions(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=40, verbose_name=_('наименование'), db_index=True, null=True, blank=True)
    description = models.TextField(verbose_name=_('Описание'), db_index=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата начало предложения'), db_index=True, null=True)
    active = models.BooleanField(verbose_name=_('Статус акции'), db_index=True, default=False)

    class Meta:
        db_table = 'Promotions'
        verbose_name = _('Предложение')
        verbose_name_plural = _('Предложения')

class Stock(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=40, verbose_name=_('наименование'), db_index=True, null=True, blank=True)
    description = models.TextField(verbose_name=_('Описание'), db_index=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата начало акции'), db_index=True, null=True)
    active = models.BooleanField(verbose_name=_('Статус акции'), db_index=True, default=False)

    class Meta:
        db_table = 'Stock'
        verbose_name = _('Акция')
        verbose_name_plural = _('Акции')