import random
import string

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app_blog.models import Blog, Profile
from app_blog.forms import MyUserRegister

NUMBER_OF_ITEMS = 10

USER = 'TEST'
USER_2 = 'TEST2'
PASSWORD = 'test21312414'
USER_REGISTER = 'TEST_REGISTER'
TEST_PHONE = '2341421424'

class UserRegisterTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        letters = string.ascii_lowercase
        author = title = description = ''.join(random.choice(letters) for i in range(NUMBER_OF_ITEMS))

        for item_index in range(NUMBER_OF_ITEMS):
            Blog.objects.create(
                id=item_index,
                author=author,
                title=title,
                description=description,
            )

        test_user = User.objects.create_user(username=USER, password=PASSWORD)
        test_user.save()
        user_profile = Profile.objects.create(
            user=test_user,
            phone=TEST_PHONE
        )
        user_profile.save()


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
        response_register_post = self.client.post(reverse('register'), {'username': USER_2, 'password1': PASSWORD, 'password2': PASSWORD, 'phone': '99999'})
        #Сюда же должно добавиться данные которые я ввел выше строчкой?
        form_data = MyUserRegister(response_register_post)
        print(form_data)
        self.assertTrue(form_data.is_valid())
        self.assertRedirects(response_register_post, reverse('index'))
        self.assertEqual(response_register_post.status_code, 302)

        current_user = User.objects.get(username=USER_2)
        self.assertEqual(current_user.profile.phone, '00000')

        #тут еще проверку что пользователь зарегался



    # def test_profile_info(self):
    #     response_profile_info = self.client.get(reverse('profile_info'))
    #     self.assertEqual(response_profile_info.status_code, 200)
    #     self.assertTemplateUsed(response_profile_info, 'users/profile_user.html')
    #     #проверка что данные пользователя вывелись


    # def test_profile_user_edit(self):
    #     response_profile_user_edit = self.client.get(reverse('profile_user_edit'))
    #     self.assertEqual(response_profile_user_edit.status_code, 200)
    #     self.assertTemplateUsed(response_profile_user_edit, 'users/profil_user_edit.html')
    #     #Проверка что данные вывелись
    #







        # response_6 = self.client.get(reverse('created_blog'))
        # response_7 = self.client.get(reverse('upload_file_blog'))
        # response_8 = self.client.get(reverse('restore_password'))
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


        # ===============================================




    # blog_info
    # self.assertEqual(response_blog.status_code, 200)
    # self.assertTemplateUsed(response_blog, reverse('blog_info'))
    # response_blog = self.client.get(reverse('blog_info', kwargs={'blog_id': self.test_blog.id}))
