import os
import random
import string

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_blog.models import Blog, Profile
from app_blog.forms import MyUserRegister
from django.test import Client

from web_blog.settings import BASE_DIR

NUMBER_OF_ITEMS = 10

USER = 'TEST'
USER_2 = 'TEST2'
PASSWORD = 'test21312414'
USER_REGISTER = 'TEST_REGISTER'
TEST_PHONE = '2341421424'
USER_NAME = 'TEST_NAME'
USER_LAST_NAME = 'TEST_LAST_NAME'

class UserRegisterTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        letters = string.ascii_lowercase
        # author = title = description = ''.join(random.choice(letters) for i in range(NUMBER_OF_ITEMS))


        test_user = User.objects.create_user(username=USER, password=PASSWORD, first_name=USER_NAME, last_name=USER_LAST_NAME)

        test_user.save()
        user_profile = Profile.objects.create(
            user=test_user,
            phone=TEST_PHONE
        )
        user_profile.save()
        author = User.objects.get(username=USER).username
        title = description = ''.join(random.choice(letters) for i in range(NUMBER_OF_ITEMS))
        for item_index in range(NUMBER_OF_ITEMS):
            Blog.objects.create(
                id=item_index,
                author=author,
                title=title,
                description=description,
            )



    def test_items_exsists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_items_number(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['blog_list']) == NUMBER_OF_ITEMS)


    def test_login(self):

        response_login = self.client.get(reverse('login'))
        self.assertEqual(response_login.status_code, 200)
        self.assertTemplateUsed(response_login, 'users/login.html')
        login = self.client.login(username=USER, password=PASSWORD)
        self.assertEqual(response_login.status_code, 200)

        #Еще раз првоерим чтов  БД есть такой пользователь
        temp = User.objects.get(username=USER)
        self.assertEqual(temp.username, USER)


    def test_register(self):
        response_register = self.client.get(reverse('register'))
        self.assertEqual(response_register.status_code, 200)
        self.assertTemplateUsed(response_register, 'users/register.html')
        #нвоый пользователь
        response_register_post = self.client.post(reverse('register'), {'username': USER_2, 'password1': PASSWORD, 'password2': PASSWORD, 'phone': '99999'})
        self.assertRedirects(response_register_post, reverse('index'))
        self.assertEqual(response_register_post.status_code, 302)
        current_user = User.objects.get(username=USER_2)
        self.assertEqual(current_user.profile.phone, '99999')


        #если такой пользователь есть
        response_register_post_new = self.client.post(reverse('register'),
                                                  {'username': USER,
                                                   'password1': PASSWORD,
                                                   'password2': PASSWORD,
                                                   'phone': '99999'})

        self.assertEqual(response_register_post_new.status_code, 200)





    def test_profile_info(self):
        login = self.client.login(username=USER, password=PASSWORD)
        response_profile_info = self.client.get(reverse('profile_info'))
        self.assertEqual(response_profile_info.status_code, 200)
        self.assertTemplateUsed(response_profile_info, 'users/profile_user.html')



    def test_profile_user_edit(self):
        login = self.client.login(username=USER, password=PASSWORD)
        response_profile_user_edit = self.client.get(reverse('profile_user_edit'))
        self.assertEqual(response_profile_user_edit.status_code, 200)
        self.assertTemplateUsed(response_profile_user_edit, 'users/profil_user_edit.html')
        old_first_name = User.objects.get(username=USER).first_name
        old_last_name = User.objects.get(username=USER).last_name
        response_post = self.client.post(reverse('profile_user_edit'), {'name': 'NEW_NAME', 'last_name': 'NEW_LAST_NAME'})
        new_first_name = User.objects.get(username=USER).first_name
        new_last_name = User.objects.get(username=USER).last_name
        self.assertEqual(response_post.status_code, 302)
        self.assertRedirects(response_post, reverse('profile_info'))
        #Тут проверим что изменились введеные даные
        self.assertNotEqual(old_first_name, new_first_name)
        self.assertNotEqual(old_last_name, new_last_name)


    def test_created_blog(self):
        response = self.client.get(reverse('created_blog'))
        self.assertRedirects(response, reverse('index'))

        login = self.client.login(username=USER, password=PASSWORD)
        response_login = self.client.get(reverse('created_blog'))
        self.assertEqual(response_login.status_code, 200)
        author = User.objects.get(username=USER).username
        response_post = self.client.post(reverse('created_blog'), {'title': 'TEST_TITLE', 'description': 'TEST_DESCRIPTION', 'multi_link_file_img': 'LINK_TEST', 'author': author})
        self.assertRedirects(response_post, reverse('index'))



    def test_blog_info(self):
        resp = self.client.get(reverse('blog_info', kwargs={'blog_id': 1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/blog_full_info.html')

    def test_upload_file(self):
        #До логирования
        response = self.client.get(reverse('upload_file_blog'))
        self.assertRedirects(response, reverse('index'))

        #после авторизации
        login = self.client.login(username=USER, password=PASSWORD)
        response_login = self.client.get(reverse('upload_file_blog'))
        self.assertEqual(response_login.status_code, 200)

        c = Client()
        link_file = os.path.join(BASE_DIR, 'ALL_DATA_FILES/FILES_TEST/')
        name_file = 'book2.csv'
        file = link_file + name_file

        with open(file) as fp:
            c.post(reverse('upload_file_blog'), {'username': USER, 'file_csv_form': fp})



        # response_9 = self.client.get(reverse('succes'))
        #
        # #created_blog
        # self.assertEqual(response_6.status_code, 200)
        # self.assertTemplateUsed(response_6, reverse('created_blog'))
        #
        # #upload_file_blog
        # self.assertEqual(response_7.status_code, 200)
        # self.assertTemplateUsed(response_7, reverse('upload_file_blog'))
        #
        # #restore_password
        # self.assertEqual(response_8.status_code, 200)
        # self.assertTemplateUsed(response_8, reverse('restore_password'))
        #
        # #succes
        # self.assertEqual(response_9.status_code, 200)
        # self.assertTemplateUsed(response_9, 'complete/succes.html')
        #
        #
        #
        # response_logout = self.client.get(reverse('logout'))
        # # logout
        # self.assertEqual(response_logout.status_code, 302)
        # self.assertRedirects(response_logout, (reverse('index')))







    # blog_info
    # self.assertEqual(response_blog.status_code, 200)
    # self.assertTemplateUsed(response_blog, reverse('blog_info'))
    # response_blog = self.client.get(reverse('blog_info', kwargs={'blog_id': self.test_blog.id}))
