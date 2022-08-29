# Generated by Django 4.0.2 on 2022-03-15 19:49

import app_helpdream.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.TextField(db_index=True, null=True, verbose_name='Текст сообщения')),
                ('data_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Инфо о комменте',
                'verbose_name_plural': 'Информация о коментариях',
                'db_table': 'Comments',
                'ordering': ['-data_created'],
            },
        ),
        migrations.CreateModel(
            name='PaymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(db_index=True, max_length=30, null=True, verbose_name='Какой банк')),
                ('amount', models.IntegerField(db_index=True, null=True, verbose_name='Сумма денег')),
                ('dt_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата совершении оплаты')),
                ('other_info', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Еще какая то информация')),
                ('whom', models.ForeignKey(blank=True, default='пусто', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователя кому перечислил денег')),
            ],
            options={
                'verbose_name': 'История операции',
                'verbose_name_plural': 'История операций',
                'db_table': 'PaymentHistory',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')], db_index=True, default='не указан', max_length=100, verbose_name='Выберите пол')),
                ('avatar', models.ImageField(blank=True, db_index=True, default='avatars/user-avatar.svg', upload_to='avatars/', verbose_name='Аватарка')),
                ('creadet_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата создания')),
                ('phone', models.CharField(blank=True, db_index=True, default='', max_length=40, verbose_name='Телефон')),
                ('my_balance', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Баланс')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='возраст')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')),
                ('help_balanced', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='на сколько помогли')),
                ('rank', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='ранк')),
                ('max_dream_created', models.IntegerField(default=5, verbose_name='Сколько создать мечт можно')),
                ('max_dream_price', models.IntegerField(default=15000, verbose_name='Максимальная сумма мечты')),
                ('super_status', models.BooleanField(blank=True, default=False, verbose_name='супер статус')),
                ('img', models.ImageField(blank=True, db_index=True, default='img_status/zvezda0.png', upload_to='img_status/', verbose_name='ранг')),
                ('place', models.IntegerField(blank=True, null=True, verbose_name='слот для расчета места в топе')),
                ('all_info_user', models.BooleanField(blank=True, db_index=True, default=False, verbose_name='Значек что вся инфа юзера заполнена')),
                ('payment_history', models.ManyToManyField(blank=True, db_index=True, to='app_helpdream.PaymentHistory', verbose_name='Модель историй оплаты')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'профиль',
                'verbose_name_plural': 'профили',
                'db_table': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='WhoHelpMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.TextField(blank=True, db_index=True, null=True, verbose_name='Сообщение при донате')),
                ('who_price', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='на сколько помогли ')),
                ('place_number', models.IntegerField(blank=True, default=0, verbose_name='порядковый номер для ограниченого вывода в завершенных')),
                ('data_popolnenia', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('help_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.profile', verbose_name='Профиль кто помог')),
            ],
            options={
                'verbose_name': 'мечта которой помогли',
                'verbose_name_plural': 'мечты которым помогли',
                'db_table': 'WhoHelpMe',
                'ordering': ['-data_popolnenia'],
            },
        ),
        migrations.CreateModel(
            name='WhoHelpMeBoxDream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_win_price', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='сколько выйграл ')),
                ('avatar', models.ImageField(blank=True, db_index=True, default='avatar_boxdream/ava_boxdream.png', upload_to='avatar_boxdream/', verbose_name='Аватарка_boxdream')),
                ('data_popolnenia', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WriteDeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=25, null=True, verbose_name='название мечты')),
                ('description', models.TextField(db_index=True, null=True, verbose_name='описание мечты')),
                ('price', models.IntegerField(db_index=True, default=0, null=True, verbose_name='сумма на мечту')),
                ('creadet_at_dream', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата создания')),
                ('creadet_at_dream_time', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата создания для расчета времени заявки')),
                ('updated_dream', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата обновления')),
                ('dream_is_active', models.BooleanField(blank=True, db_index=True, default=True, verbose_name='мечта активна')),
                ('dream_is_complete', models.BooleanField(blank=True, db_index=True, default=False, verbose_name='мечта завершена')),
                ('help_price', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Сколько собрали уже на мечту')),
                ('place', models.IntegerField(blank=True, null=True, verbose_name='слот для расчета позиции ')),
                ('days_end', models.IntegerField(blank=True, default=30, verbose_name='Сколько дней до завершения мечты')),
                ('number_for_draw', models.IntegerField(blank=True, default=0)),
                ('comments', models.ManyToManyField(blank=True, db_index=True, to='app_helpdream.Comments', verbose_name='Модели комментария')),
                ('where_dream', models.ManyToManyField(blank=True, db_index=True, to='app_helpdream.WhoHelpMe', verbose_name='Профиль кто помог этой мечте')),
                ('where_dream_box', models.ManyToManyField(blank=True, db_index=True, to='app_helpdream.WhoHelpMeBoxDream', verbose_name='Профиль BOXDREAM кто помог этой мечте')),
                ('who_dream', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.profile', verbose_name='Чья эта мечта')),
            ],
            options={
                'verbose_name': 'Мечта',
                'verbose_name_plural': 'Мечты пользователей',
                'db_table': 'WriteDeam',
            },
        ),
        migrations.CreateModel(
            name='WinDream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_help_box', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Сколько денег мечта получила через BOXDREAM')),
                ('who_dream_box', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.writedeam', verbose_name='Какой мечте помогли')),
            ],
        ),
        migrations.CreateModel(
            name='TotalBoxDream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Баланс BOXDREAM')),
                ('creadet_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата создания')),
                ('count_win_box', models.IntegerField(db_index=True, default=1, verbose_name='Какой по счету розыгрыш')),
                ('who_help_boxdream', models.ManyToManyField(blank=True, db_index=True, to='app_helpdream.WhoHelpMe', verbose_name='Профиль кто помог BOXDREAM')),
            ],
            options={
                'db_table': 'TotalBoxDream',
                'ordering': ['-creadet_at'],
            },
        ),
        migrations.CreateModel(
            name='ImgWriteDream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, db_index=True, null=True, upload_to=app_helpdream.models.user_directory_path, verbose_name='фото')),
                ('img_dream', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.writedeam', verbose_name='фотки')),
            ],
            options={
                'db_table': 'ImgWriteDream',
            },
        ),
        migrations.CreateModel(
            name='HistoryBoxDream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_win', models.IntegerField(db_index=True, default=1, verbose_name='номер розыгрыша')),
                ('data_win_box', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата розыгрыша')),
                ('win_dream', models.ManyToManyField(blank=True, db_index=True, to='app_helpdream.WinDream', verbose_name='Мечта с параметрами кто выграл')),
            ],
            options={
                'db_table': 'HistoryBoxDream',
                'ordering': ['-data_win_box'],
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_helpdream.profile', verbose_name='Кто написал комментарий'),
        ),
    ]