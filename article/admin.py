from django.contrib import admin
from .models import Article
# from .models import Contributor


class ArticleA(admin.ModelAdmin):
    list_display = ('type', 'title', 'by', 'profile')


admin.site.register(Article, ArticleA)
# admin.site.register(Contributor)

# Register your models here.

admin.site.site_header = "NewsWebApp Admin"
