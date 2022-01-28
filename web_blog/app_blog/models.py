from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


#Это добавление к стандартному User новые поля
class Profile(models.Model):

    STATUS_CHOISE = [
        ('Мужской', _('Man')),
        ('Женский', _('Girl'))
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    phone = models.CharField(max_length=20, verbose_name=_('Phone'), db_index=True)
    gender = models.CharField(max_length=100, choices=STATUS_CHOISE, verbose_name=_('Select gender'), db_index=True, default=_('Man'))
    avatar = models.ImageField(upload_to='avatars/', verbose_name=_('Select file'), db_index=True, default='')
    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'Profile'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

class Blog(models.Model):

    def __str__(self):
        return self.title

    author = models.CharField(max_length=60, verbose_name=_('Author blog'), db_index=True )
    title = models.CharField(max_length=60, verbose_name=_('Title blog'), db_index=True)
    description = models.TextField(blank=True, verbose_name=_('Description blog'), db_index=True)
    creadet_at = models.DateTimeField(auto_now_add=True, verbose_name=_('creadet at'), db_index=True)
    multi_link_file_img = models.TextField(verbose_name=_('Link photo'), db_index=True, default='')



    def min_description(self):

        return self.description[:100] + '...'

    def data_blog(self):
        temp = str(self.creadet_at)
        data = temp[:10]
        time_x = temp[10:]
        time = time_x[:6]
        data_str = f'Дата: {data}, время: {time}'
        return data_str

    class Meta:
        db_table = 'Blog'
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')


class BlogPhoto(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default='')
    file_img = models.ImageField(upload_to='img_blog/', verbose_name=_('Photo'), db_index=True, default='')

    class Meta:
        db_table = 'BlogPhoto'
        verbose_name = _('blogPhoto')
        verbose_name_plural = _('blogPhotos')