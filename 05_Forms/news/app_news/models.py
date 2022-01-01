from django.db import models



class User(models.Model):

    def __str__(self):
        return self.username

    username = models.CharField(max_length=30, verbose_name='Имя', db_index=True)
    password = models.CharField(max_length=20, verbose_name='Пароль', db_index=True)
    first_name = models.CharField(max_length=20, verbose_name='Фамилия', db_index=True)
    second_name = models.CharField(max_length=20, verbose_name='Отчество', db_index=True)
    email = models.EmailField(verbose_name='mail', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', db_index=True)
    is_active_user = models.BooleanField(verbose_name='актив', db_index=True)

    class Meta:
        db_table = 'Users'
        ordering = ['created_at']


class MyNews(models.Model):

    def __str__(self):
        return self.titleNews

    titleNews = models.CharField(max_length=200, verbose_name='Заголовок новости', db_index=True)
    description = models.TextField(default='', verbose_name='описание', db_index=True)
    created_news = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', db_index=True)
    updated_news = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', db_index=True)
    is_active_news = models.BooleanField(verbose_name='Активность новости', db_index=True)

    class Meta:
        db_table = 'News'


class MyComments(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, verbose_name='Имя', db_index=True)
    description = models.TextField(default='', verbose_name='описание', db_index=True)

    news = models.ForeignKey('MyNews', default=None, null=True, on_delete=models.CASCADE,
                                       related_name='News', verbose_name='новость')

    class Meta:
        db_table = 'Comments'
        ordering = ['news']
