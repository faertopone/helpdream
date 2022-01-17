from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default='+70000000000', verbose_name='Телефон', db_index=True)
    city = models.CharField(max_length=40, blank=True, verbose_name='Город', db_index=True)
    date_of_birth = models.DateTimeField(verbose_name='дата рождения', db_index=True)
    flag_veryfication = models.BooleanField(default=False, verbose_name='Флаг верификации', db_index=True)
    count_news = models.IntegerField(default=0, verbose_name='Количество новостей', db_index=True)

    #в Модели что бы вывести модернезирвоанные данные
    def new_date_of_birth(self):
        data = self.date_of_birth
        data_str = str(data)
        new_data = data_str[:10]
        return str(new_data)

    class Meta:
        db_table = 'Profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        permissions = (
            ('veryfication', 'Верифицирован пользователя'),
            ('remove_veryfication', 'Убрать верификацию пользователя'),
            ('add_veryfication', 'Добавить верификацию пользователя'),
            ('moderator_time', 'Проверять новость и давать право на публикацию')

        )

    def __str__(self):
        return self.user.username
