from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import WriteDeam


class DreamsSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return WriteDeam.objects.select_related('who_dream').order_by('-creadet_at_dream').filter(dream_is_active=True).all()

    def lastmod(self, obj: WriteDeam):
        return obj.creadet_at_dream


# Статические страницы
class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'information'

    def items(self):
        return ['about']

    def location(self, item):
        return reverse(item)