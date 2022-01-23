from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


#Это добавление к стандартному User новые поля
class Profile(models.Model):

    STATUS_CHOISE = [
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(default='', verbose_name='Телефон', db_index=True)
    gender = models.CharField(max_length=100, choices=STATUS_CHOISE, verbose_name='Ваш пол', db_index=True, default='Мужской')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Выберите фаил', db_index=True, default='')
    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'Profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class Blog(models.Model):

    def __str__(self):
        return self.title

    author = models.CharField(max_length=60, verbose_name='Автор блога', db_index=True )
    title = models.CharField(max_length=60, verbose_name='Название новости', db_index=True)
    description = models.TextField(blank=True, verbose_name='Описание новости', db_index=True)
    creadet_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', db_index=True)
    file_img = models.ImageField(upload_to='img_blog/', verbose_name='Фото', db_index=True, default='')
    link_file_img = models.CharField(max_length=300, verbose_name='Ссылка', db_index=True, default='')
    multi_link_file_img = models.TextField(verbose_name='Ссылка на фото', db_index=True, default='')



    def min_description(self):

        return self.description[:100]

    def data_blog(self):
        temp = str(self.creadet_at)
        data = temp[:10]
        time_x = temp[10:]
        time = time_x[:6]
        data_str = f'Дата: {data}, время: {time}'
        return data_str

    class Meta:
        db_table = 'Blog'
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'