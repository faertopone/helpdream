from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbose_name='Заголовок')
    description = models.TextField(default='', verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.title
