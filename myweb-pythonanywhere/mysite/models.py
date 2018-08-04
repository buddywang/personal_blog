from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from read_statistics.models import ReadNumExpandMethod

class BlogType(models.Model):
    blog_type = models.CharField('类别',max_length=10)

    class Meta:
        verbose_name_plural = '文章分类'
        verbose_name = '类别'
    def __str__(self):
        return  self.blog_type

class Article(models.Model,ReadNumExpandMethod):#继承了ReadNumExpandMethod抽象类
    title = models.CharField("标题",max_length=100)
    date = models.DateTimeField("发布时间",auto_now_add=True)
    changedate = models.DateTimeField('创建时间',auto_now=True)
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=1)
    blogtype = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    content = RichTextUploadingField('内容')

    class Meta:
        verbose_name_plural = '文章管理'
        verbose_name = '文章'
        ordering = ['-changedate',]

    def __str__(self):
        return  self.title