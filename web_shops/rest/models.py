from django.db import models

# Create your models here.


class ItemModel(models.Model):
    """
    Модель Товаров.
    """
    name = models.CharField(max_length=200, verbose_name='название', null=True)
    description = models.TextField(blank=True, verbose_name='описание')
    weight = models.FloatField(verbose_name='вес')





class AuthorBook(models.Model):
    """
    Модель Автора книг.
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=40, verbose_name='имя', null=True)
    lastname = models.CharField(max_length=40, verbose_name='фамилия', null=True)
    yearofbirth = models.DateField(verbose_name='Дата рождения', null=True)


    class Meta:
        db_table = 'AuthorBook'



class Book(models.Model):
    """
    Модель Книг.
    """

    def __str__(self):
        return self.name

    name = models.CharField(max_length=40, verbose_name='Название книги', null=True)
    isbn = models.IntegerField(verbose_name='международный стандартный книжный номер', null=True)
    yearofissue = models.DateField(verbose_name='Год выпуска', null=True)
    numberofpages = models.IntegerField(verbose_name='Количество страниц', null=True)
    author_book = models.ForeignKey(AuthorBook, on_delete=models.CASCADE, null=True, verbose_name='Автор книги')

    class Meta:
        db_table = 'Book'

