from django.db import models

class Vacancy(models.Model):

    is_active = models.BooleanField(default=False, verbose_name='Активность', db_index=True)
    title = models.CharField(max_length=30, verbose_name='Заголовок', db_index=True)
    description = models.TextField(default='', verbose_name='Описание', db_index=True)
    publisher = models.CharField(max_length=50, verbose_name='Кто опубликовал', db_index=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, db_index=True)
    published_at = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        permissions = (
            ('Can_publish', 'Может публиковать'),
        )

    def __str__(self):
        return self.title


class Summary(models.Model):

    title = models.CharField(max_length=50, verbose_name='Заголовок', db_index=True)
    creatde_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, db_index=True)
    publisher_at = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True, db_index=True)
    description = models.TextField(default='', verbose_name='Описание', db_index=True)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Все резюме'


    def __str__(self):
        return self.title