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