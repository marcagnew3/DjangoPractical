from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'content', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']


admin.site.register(Article, ArticleAdmin)