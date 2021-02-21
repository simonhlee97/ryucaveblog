from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from blog.views import about


sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('about/', about, name='about'),
    path('ryucaveadmin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
