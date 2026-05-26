from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class ProjectSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ['portfolio:index']

    def location(self, obj):
        return reverse(obj)