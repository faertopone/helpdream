from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import News


class NewsSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return News.objects.filter(is_published=True).all()

    def lastmod(self, obj: News):
        return obj.created_at


# Статические страницы
class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'information'

    def items(self):
        return ['contacts', 'about']

    def location(self, item):
        return reverse(item)