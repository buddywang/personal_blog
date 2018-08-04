from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ReadNum(models.Model):
    read_num = models.IntegerField('阅读量',default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name_plural = '文章计数'
        verbose_name = '计数'
    def __str__(self):
        return  self.read_num

#通用计数抽象类
class ReadNumExpandMethod():
    def read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct,object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0