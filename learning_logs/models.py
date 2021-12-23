from typing import Text
from django.db import models
from django.db.models.base import Model
class Topic(models.Model):
    '''用户学习主题'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        '''返回模型字符串表示'''
        return self.text
# Create your models here.
