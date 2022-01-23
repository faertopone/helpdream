from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    id_item = models.CharField(max_length=100, verbose_name='id')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')


class File(models.Model):
    file = models.FileField(upload_to='files/', verbose_name='Выберите фаил', db_index=True)
    description = models.TextField(blank=True, verbose_name='Описание к этому файлу', db_index=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', db_index=True)

    class Meta:
        db_table = 'File'

    def __str__(self):
        return str(self.file)