# -*- coding: utf-8 -*-
from django.db import models
  
# 上传图片  设置media以显示图片
class Course(models.Model):
    image = models.ImageField(default='', upload_to='image/', verbose_name='图片logo', max_length=100)