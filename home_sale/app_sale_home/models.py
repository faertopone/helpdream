from django.db import models


class Housing(models.Model):
    name = models.CharField(max_length=40, verbose_name='имя жилья')
    description = models.TextField(blank=True, verbose_name='описания жилья')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жильё'
        verbose_name_plural = 'Жильёшки'


class TypeHousing(models.Model):
    name = models.CharField(max_length=40, verbose_name='тип помещения')
    description = models.TextField(blank=True, verbose_name='описание помещения')
    hous = models.OneToOneField(Housing, verbose_name='в каком доме', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.hous.name

    class Meta:
        verbose_name = 'Тип жилья'
        verbose_name_plural = 'Типы жилья'




class NumberRooms(models.Model):

    rooms_count = models.IntegerField(default=0, verbose_name='количество комнат')
    hous = models.OneToOneField(Housing, verbose_name='в каком доме',  on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.hous.name

    class Meta:
        verbose_name = 'Количество комнат'
        verbose_name_plural = 'Количество комнат'


class News(models.Model):

    title = models.CharField(max_length=60, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст новости', null=True)
    is_published = models.BooleanField(default=False, verbose_name='опубликовать')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'