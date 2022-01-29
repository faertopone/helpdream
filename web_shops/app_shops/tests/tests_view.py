import os
import random
import string

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_shops.models import Profile, Shops, ProfilePhotos


NUMBER_OF_ITEMS = 5
USERNAME = 'TEST'
USERNAME_1 = 'TESsdffT'
PASSWORD = 'sdkljgngz231'
FIRST_NAME = 'sdsggs'
EMAIL = 'dsgdgs@mail.ru'
GENDER = 'Мужской'
PHONE = '095-159-035'
ADRESS = 'ksdjlkgs.kg'

class UserRegisterTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Создали юзера
        test_user = User.objects.create_user(username=USERNAME, password=PASSWORD, first_name=FIRST_NAME, email=EMAIL)
        test_user.save()
        user_profile = Profile.objects.create(
            user=test_user,
            phone=PHONE,
            gender=GENDER
        )
        user_profile.save()
        temp = test_user.username

        ProfilePhotos.objects.create(photo=user_profile, photo_img=None)

        #Создали запись из 10 магазинов
        for item_index in range(NUMBER_OF_ITEMS):
            name_c = temp + str(item_index)
            adress_c = ADRESS + str(item_index)
            tel = PHONE + str(item_index)
            Shops.objects.create(
                name=name_c,
                adress=adress_c,
                tel=tel,
            )



    def test_items_exsists_at_desired_location(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        login = self.client.login(username=USERNAME, password=PASSWORD)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        response_post = self.client.post(reverse('register'), {'username': USERNAME_1, 'password1': PASSWORD, 'password2': PASSWORD, 'phone': PHONE, 'email': EMAIL, 'gender': GENDER})
        #Форма прошла  и валидна
        self.assertRedirects(response_post, reverse('index'))

    def test_login(self):
        response_login = self.client.get(reverse('index'))
        self.assertEqual(response_login.status_code, 200)
        self.assertTemplateUsed(response_login, 'index.html')
        login = self.client.login(username=USERNAME, password=PASSWORD)
        self.assertEqual(response_login.status_code, 200)

        #Еще раз првоерим чтов  БД есть такой пользователь
        temp = User.objects.get(username=USERNAME)
        self.assertEqual(temp.username, USERNAME)

    def test_ProfileInfo(self):
        #До логина, перенапраит на главную
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, reverse('index'))
        #После логина позволит смотреть профиль
        login = self.client.login(username=USERNAME, password=PASSWORD)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_user.html')

    def test_ShopsView(self):
        response = self.client.get(reverse('shops_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops_list.html')

        #Првоерка что вывел все списки магазинов
        self.assertTrue(len(response.context['shops']) == NUMBER_OF_ITEMS)