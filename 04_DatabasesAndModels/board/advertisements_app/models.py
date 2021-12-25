from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbose_name='Заголовок', db_index=True)
    description = models.TextField(default='', verbose_name='описание', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', db_index=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', db_index=True)
    price = models.FloatField(verbose_name='цена', default=0, db_index=True)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0, db_index=True)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements')

    type = models.ForeignKey('Type', default=None, null=True, on_delete=models.CASCADE, related_name='type')


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']

class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)


#    Тип   обьявления
class Type(models.Model):
    name = models.CharField(max_length=100)