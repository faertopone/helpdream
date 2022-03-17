from django.db import models



class Blog(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'Blog'
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=40, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    is_published = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Post'
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title