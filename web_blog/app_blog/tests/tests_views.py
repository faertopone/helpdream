import random
import string

from django.test import TestCase
from django.urls import reverse

from app_blog.models import Blog

NUMBER_OF_ITEMS = 10

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

    def test_items_exsists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_items_number(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['blog_list']) == NUMBER_OF_ITEMS)
