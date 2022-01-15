from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=40, blank=True, verbose_name='Город', db_index=True)
    date_of_birth = models.DateTimeField(verbose_name='дата рождения', db_index=True)

    #в Модели что бы вывести модернезирвоанные данные
    def new_date_of_birth(self):
        data = self.date_of_birth
        data_str = str(data)
        print(data_str, 'дата стр')
        new_data = data_str[:10]
        print(new_data, 'Дата после среза')
        return str(new_data)

    class Meta:
        db_table = 'Profile'

