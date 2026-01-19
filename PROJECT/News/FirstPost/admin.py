from django.contrib import admin
from .models import NewsArticles
class NewsArticlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'articleId', 'articleImg', 'articleName', 'articleContent', 'publishDate', 'authorId']
    list_filter = ['authorId', 'publishDate']
    ordering = ['id', 'articleName', 'publishDate', 'authorId']
    list_editable = ['articleId', 'articleImg', 'articleName', 'articleContent', 'publishDate', 'authorId']
admin.site.register(NewsArticles, NewsArticlesAdmin)



