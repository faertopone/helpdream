from django.contrib.sitemaps import Sitemap
from .models import News


class NewsSiteMap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return News.objects.filter(is_published=True).all()

    def lastmod(self, obj: News):
        return obj.created_at