from django.contrib import admin
from .models import Article,BlogType

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','author','blogtype','read_num','date','changedate')

class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('blog_type',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(BlogType,BlogTypeAdmin)