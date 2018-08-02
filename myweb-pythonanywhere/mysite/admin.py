from django.contrib import admin
from .models import Article,BlogType,ReadNum
from django.contrib.auth.models import User

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','blogtype','read_num','date','changedate')

class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('blog_type',)

class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num','blog',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(BlogType,BlogTypeAdmin)
admin.site.register(ReadNum,ReadNumAdmin)