import random
import string

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

USER_EMAIL = 'test@company.com'
USER_NAME = 'TEST'
OLD_PASSWORD = 'testpassord'


class RestorePasswordTest(TestCase):


    #Проверяем что такой путь есть и правильный
    def test_restore_password_url_exists_at_desired_location(self):
        response = self.client.get('/restore_password/')
        self.assertEqual(response.status_code, 200)

    # Проверяем что по такому пути грузиться верное представление HTML страницы
    def test_restore_password_uses_correct_template(self):
        response = self.client.get(reverse('restore_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Users/restore_password.html')




    def test_post_restore_password(self):
        user = User.objects.create(username=USER_NAME, email=USER_EMAIL)
        response = self.client.post(reverse('restore_password'), {'email': USER_EMAIL})

        #200 если перенаравление идет HttpResponse, и редирект работает или если HttpResponseRedirect то 302
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('succes'))
        from django.core.mail import outbox
        self.assertEqual(len(outbox), 1)
        self.assertIn(USER_EMAIL, outbox[0].to)



    def test_if_password_was_changed(self):
        user = User.objects.create(username=USER_NAME, email=USER_EMAIL)
        user.set_password(OLD_PASSWORD)
        user.save()
        old_password_hash = user.password

        response = self.client.post(reverse('restore_password'), {'email': USER_EMAIL})
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertNotEqual(old_password_hash, user.password)