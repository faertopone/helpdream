"""helpdream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from app_helpdream.sitemap import DreamsSiteMap, StaticViewSitemap
from django.conf import settings


# сюда добавить все что хотим в карту
sitemaps = {
    'WriteDeam': DreamsSiteMap,
    'static': StaticViewSitemap,
}






urlpatterns = [
    # для документирования(обезателньо сверху)
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    # ЧТо бы работала локализация
    path('i18n', include('django.conf.urls.i18n')),
    path('', include('app_helpdream.urls')),
    #Для карты сайта
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('ckeditor/', include('ckeditor_uploader.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
