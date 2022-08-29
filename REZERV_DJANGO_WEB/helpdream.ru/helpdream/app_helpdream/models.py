from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.datetime_safe import datetime
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField




#История оплаты
class PaymentHistory(models.Model):

    def __str__(self):
        return self.whom

    bank = models.CharField(max_length=30, verbose_name=_('Какой банк'), null=True, db_index=True)
    #Кому
    whom = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Пользователя кому перечислил денег'), default='пусто', blank=True, db_index=True)
    amount = models.IntegerField(verbose_name=_('Сумма денег'), null=True, db_index=True)
    dt_created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_('Дата совершении оплаты'))
    other_info = models.CharField(max_length=100, verbose_name=_('Еще какая то информация'), null=True, db_index=True, blank=True)

    class Meta:
        db_table = 'PaymentHistory'
        verbose_name = _('История операции')
        verbose_name_plural = _('История операций')


class Profile(models.Model):

    """
    Модель Профиля. дополнение к стандартным полям USER
    """
    def __str__(self):
        return self.user.username




    STATUS_CHOISE = [
        ('Мужской', _('Мужской')),
        ('Женский', _('Женский'))
    ]



    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    gender = models.CharField(max_length=100, choices=STATUS_CHOISE, verbose_name=_('Выберите пол'), db_index=True, default=_('не указан'), blank=True)
    avatar = models.ImageField(upload_to='avatars/', verbose_name=_('Аватарка'), default='avatars/user-avatar.svg', db_index=True, blank=True)
    creadet_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'), db_index=True, null=True)

    phone = models.CharField(max_length=40, verbose_name=_('Телефон'), db_index=True, default='', blank=True)
    my_balance = models.IntegerField(verbose_name=_('Баланс'), db_index=True, blank=True, default=0)
    age = models.IntegerField(verbose_name=_('возраст'), blank=True, null=True)
    birthday = models.DateTimeField(verbose_name=_('Дата рождения'), null=True, blank=True)
    help_balanced = models.IntegerField(verbose_name=_('на сколько помогли'), db_index=True, blank=True, default=0)
    rank = models.IntegerField(verbose_name=_('ранк'), default=0,
                               validators=[MinValueValidator(0), MaxValueValidator(5)])
    max_dream_created = models.IntegerField(verbose_name=_('Сколько создать мечт можно'), default=5)
    max_dream_price = models.IntegerField(verbose_name=_('Максимальная сумма мечты'), default=15000)
    super_status = models.BooleanField(verbose_name=_('супер статус'), default=False, blank=True)
    img = models.ImageField(upload_to='img_status/', verbose_name=_('ранг'), default='img_status/zvezda0.png', db_index=True,
                             blank=True)
    place = models.IntegerField(verbose_name=_('слот для расчета места в топе'), null=True, blank=True)


    #Обьекты операций каждой оплаты
    payment_history = models.ManyToManyField(PaymentHistory, verbose_name=_('Модель историй оплаты'), db_index=True, blank=True)

    all_info_user = models.BooleanField(verbose_name=_('Значек что вся инфа юзера заполнена'), db_index=True, blank=True, default=False)


    #Взависимости от ранка - возможности профиля
    def choise_rank(self):
        if self.rank == 0:
            self.max_dream_created = 5
            self.max_dream_price = 15000
            return 'img_status/zvezda0.png'
        elif self.rank == 1:
            self.max_dream_created = 8
            self.max_dream_price = 100000
            return 'img_status/zvezda1.png'
        elif self.rank == 2:
            self.max_dream_created = 10
            self.max_dream_price = 300000
            return 'img_status/zvezda2.png'
        elif self.rank == 3:
            self.max_dream_created = 15
            self.max_dream_price = 500000
            return 'img_status/zvezda3.png'
        elif self.rank == 4:
            self.max_dream_created = 25
            self.max_dream_price = 900000
            return 'img_status/zvezda4.png'
        elif self.rank == 5:
            self.max_dream_created = 100
            self.max_dream_price = 3000000
            self.super_status = True
            return 'img_status/zvezda5.png'

    class Meta:
        db_table = 'Profile'
        verbose_name = _('профиль')
        verbose_name_plural = _('профили')



class WhoHelpMe(models.Model):
    """
    Модель с хранением данных пользователей которым мне помогли
    """

    def __str__(self):
        return self.help_profile.user.username

    messages = models.TextField(verbose_name=_('Сообщение при донате'), db_index=True, blank=True, null=True)
    who_price = models.IntegerField(verbose_name=_('на сколько помогли '), db_index=True, blank=True, default=0)
    help_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, verbose_name=_('Профиль кто помог'),
                                     blank=True)

    place_number = models.IntegerField(verbose_name=_('порядковый номер для ограниченого вывода в завершенных'),
                                       default=0, blank=True)

    data_popolnenia = models.DateTimeField(auto_now_add=True,  db_index=True, null=True)


    class Meta:
        db_table = 'WhoHelpMe'
        verbose_name = _('мечта которой помогли')
        verbose_name_plural = _('мечты которым помогли')
        ordering = ['-data_popolnenia']



class WhoHelpMeBoxDream(models.Model):
    """
    Модель профиля BOXDREAM, для отчетности кто помог мечте
    """

    box_win_price = models.IntegerField(verbose_name=_('сколько выйграл '), db_index=True, blank=True, default=0)
    avatar = models.ImageField(upload_to='avatar_boxdream/', verbose_name=_('Аватарка_boxdream'), default='avatar_boxdream/ava_boxdream.png',
                               db_index=True, blank=True)

    data_popolnenia = models.DateTimeField(auto_now_add=True, db_index=True, null=True)




class Comments(models.Model):

    def __str__(self):
        return self.messages[:15]

    messages = models.TextField(null=True, verbose_name=_('Текст сообщения'), db_index=True)
    data_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'))
    author = models.ForeignKey(Profile, verbose_name=_('Кто написал комментарий'), on_delete=models.CASCADE, null=True)

    # Проверял ckeditor
    # content = RichTextField(null=True, blank=True)

    class Meta:
        db_table = 'Comments'
        verbose_name = _('Инфо о комменте')
        verbose_name_plural = _('Информация о коментариях')
        ordering = ['-data_created']



class WriteDeam(models.Model):
    """
    Модель создания мечты
    """

    def __str__(self):
        return self.title

    who_dream = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, verbose_name=_('Чья эта мечта'))
    title = models.CharField(max_length=25, verbose_name=_('название мечты'), db_index=True, null=True)
    description = models.TextField(verbose_name=_('описание мечты'), db_index=True, null=True)
    price = models.IntegerField(verbose_name=_('сумма на мечту'), db_index=True, default=0, null=True)
    creadet_at_dream = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'), db_index=True, null=True)
    creadet_at_dream_time = models.DateTimeField(auto_now_add=True,
                                           verbose_name=_('Дата создания для расчета времени заявки'), db_index=True,
                                           null=True)
    updated_dream = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', db_index=True)
    dream_is_active = models.BooleanField(default=True, verbose_name=_('мечта активна'), db_index=True, blank=True)
    dream_is_complete = models.BooleanField(default=False, verbose_name=_('мечта завершена'), db_index=True, blank=True)
    help_price = models.IntegerField(verbose_name=_('Сколько собрали уже на мечту'), db_index=True, default=0, blank=True)
    place = models.IntegerField(verbose_name=_('слот для расчета позиции '), null=True, blank=True)


    where_dream = models.ManyToManyField(WhoHelpMe, verbose_name=_('Профиль кто помог этой мечте'), db_index=True, blank=True)
    where_dream_box = models.ManyToManyField(WhoHelpMeBoxDream, verbose_name=_('Профиль BOXDREAM кто помог этой мечте'), db_index=True, blank=True)

    #Коментарии
    comments = models.ManyToManyField(Comments, verbose_name=_('Модели комментария'), db_index=True, blank=True)

    days_end = models.IntegerField(verbose_name=_('Сколько дней до завершения мечты'), blank=True, default=30)

    number_for_draw = models.IntegerField(blank=True, default=0)

    # Для карты сайта нужно
    def get_absolute_url(self):
        return reverse('detail_dream', args=[str(self.pk)])

    def mini_description(self):
        return self.description[:20] + '...'


    class Meta:
        db_table = 'WriteDeam'
        verbose_name = _('Мечта')
        verbose_name_plural = _('Мечты пользователей')




def user_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка ALL_DATA_FILES/imgdream__user_{username}__id_{user.id}/<filename>
    return 'imgdream__user_{0}__id_{1}/{2}'.format(instance.img_dream.who_dream.user.username, instance.img_dream.who_dream.id, filename)

class ImgWriteDream(models.Model):
    """
    Модель хранения фоток при создании мечты
    """
    img_dream = models.ForeignKey(WriteDeam, on_delete=models.CASCADE, null=True, verbose_name=_('фотки'))
    img = models.ImageField(upload_to=user_directory_path, verbose_name=_('фото'), db_index=True, blank=True, null=True)

    class Meta:
        db_table = 'ImgWriteDream'


class TotalBoxDream(models.Model):

    balance = models.IntegerField(verbose_name=_('Баланс BOXDREAM'), db_index=True, default=0, blank=True)
    who_help_boxdream = models.ManyToManyField(WhoHelpMe, verbose_name=_('Профиль кто помог BOXDREAM'), db_index=True,
                                         blank=True)
    creadet_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата создания'), db_index=True, null=True)
    count_win_box = models.IntegerField(verbose_name=_('Какой по счету розыгрыш'), default=1, db_index=True)


    class Meta:
        db_table = 'TotalBoxDream'
        ordering = ['-creadet_at']


class WinDream(models.Model):
    """
    Модель специальная для хранения история информации о выгрыше
    """
    amount_help_box = models.IntegerField(verbose_name=_('Сколько денег мечта получила через BOXDREAM'), db_index=True,
                                          default=0, blank=True)
    who_dream_box = models.ForeignKey(WriteDeam, on_delete=models.CASCADE, null=True,
                                      verbose_name=_('Какой мечте помогли'))



class HistoryBoxDream(models.Model):
    """
    Модель хранения истории с розыгрышем BOXDREAM
    """

    count_win = models.IntegerField(verbose_name=_('номер розыгрыша'), default=1, db_index=True)
    win_dream = models.ManyToManyField(WinDream, verbose_name=_('Мечта с параметрами кто выграл'), db_index=True, blank=True)
    data_win_box = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата розыгрыша'), db_index=True, null=True)

    class Meta:
        db_table = 'HistoryBoxDream'
        ordering = ['-data_win_box']




