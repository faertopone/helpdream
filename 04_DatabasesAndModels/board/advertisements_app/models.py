from django.db import models



class Advertisement(models.Model):
    title = models.CharField(max_length=1500, verbose_name='Заголовок', db_index=True)
    categoty_name = models.CharField(max_length=500, default='', verbose_name='Наименование рубрики', db_index=True)
    description = models.TextField(default='', verbose_name='описание', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', db_index=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', db_index=True)
    price = models.FloatField(verbose_name='цена', default=0, db_index=True)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0, db_index=True)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name='статус')
    author_content = models.ForeignKey('Author', default=None, null=True, on_delete=models.CASCADE,
                               related_name='author', verbose_name='Автор')


    def __str__(self):
        return self.title

    def modifiedСreatedTime(self):
        new_time = self.created_at
        temp = str(new_time)
        data = temp.split()
        only_data = data[0]
        time = data[1].split('.')
        string_data = str(only_data) + ' Время:' + str(time[0])
        return string_data

    def getPriceUS(self):
        return (round((self.price / 67.7), 2))


    class Meta:
        db_table = 'advertisements'
        ordering = ['title']

class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя автора', db_index=True)
    mail = models.CharField(max_length=100, verbose_name='@маил автора', db_index=True)
    phone = models.IntegerField(verbose_name='Телефон', default='----------', db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'
        ordering = ['name']

