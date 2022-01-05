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
        temp = str(self.created_news)
        data = temp[:10]
        time_x = temp[10:]
        time = time_x[:6]
        return f'{self.titlenews},   время: {time}, Дата: {data}'
    # сначало действие- потом описание (оно и в админке будет отображаться)
    STATUS_CHOISE = [
        (True, 'Активно'),
        (False, 'Не активно')
    ]
    titlenews = models.CharField(max_length=200, verbose_name='Заголовок новости', db_index=True)
    description = models.TextField(default='', verbose_name='описание', db_index=True)
    created_news = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', db_index=True)
    updated_news = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', db_index=True)
    is_active_news = models.BooleanField(verbose_name='Активность новости', db_index=True, default=False, choices=STATUS_CHOISE)
    # all_comment = models.ManyToManyField('MyComments',  verbose_name='Коментарии')



    class Meta:
        db_table = 'News'
        ordering = ['-updated_news']  # - перед парамером значит revers



class MyComments(models.Model):

    def __str__(self):
        return f'{self.name}, город ({self.city})'

        # сначало действие- потом описание (оно и в админке будет отображаться)

    STATUS_CHOISE = [
        (True, 'Удалено администратором'),
        (False, 'Комментарий норм')
    ]

    name = models.CharField(max_length=200, verbose_name='Имя', db_index=True)
    description = models.TextField(default='', verbose_name='описание', db_index=True)
    old_description = models.TextField(default='', verbose_name='Хранения комментария после удаления', db_index=True)
    created_comments = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', db_index=True)
    city = models.CharField(max_length=50, verbose_name='Город', db_index=True, default='Неизвестно')
    nickname = models.CharField(max_length=50, verbose_name='Прозвище', db_index=True, default='Неизвестно')

    comment = models.ForeignKey('MyNews', default=None, null=True, on_delete=models.CASCADE,
                                related_name='comment', verbose_name='Название новости')
    status_comment = models.BooleanField(verbose_name='статус', db_index=True, default=False, choices=STATUS_CHOISE)

    id_news_current = models.IntegerField(default=0)

    #Это сделал для того что бы в админ панели выводилось краткое описание
    def min_description(self):
        text_str = self.description
        text = list(text_str)
        if len(text) > 15:
            self.description = text_str[:15] + '...'
        else:
            self.description = text_str
        return self.description

    min_description.short_description = 'Краткое описание'

    class Meta:
        db_table = 'Comments'
        ordering = ['created_comments']
