# -*- coding: utf-8 -*-
from django.db import models

class Video(models.Model):
    SETYPE = (('爱奇艺','爱奇艺'),
        ('优酷','优酷'),
        ('乐视网','乐视网'),
        ('腾讯视频','腾讯视频'),
        ('土豆','土豆'),
        ('搜狐视频','搜狐视频'),
        ('56我乐','56我乐'),
        ('KU6.com','KU6.com'),
        ('华数TV','华数TV'),
        ('音悦Tai','音悦Tai'),
        ('芒果TV','芒果TV'),
        ('新浪视频','新浪视频'),
        ('网易视频','网易视频'),
        ('6.CN','6.CN'), 
        ('酷狗音乐','酷狗音乐'),
        ('爆米花网','爆米花网'),
        ('凤凰视频','凤凰视频'),          
        ('看看新闻','看看新闻'),        
        ('时光网','时光网'),
        ('酷我音乐','酷我音乐'),
        ('1905','1905'),
        ('糖豆','糖豆'),
        ('央视网','央视网'),              
        )
    tvname = models.CharField(max_length=20,choices=SETYPE, default=SETYPE[0][0]) 
    name = models.CharField(max_length=20,  null=True, blank=True) 
    url = models.CharField(max_length=120,  null=True, blank=True)         
    date = models.DateTimeField(auto_now=True, null=True, blank=True) #自动创建日期含时间
    def __str__(self):
        return self.name 
    
class Browse(models.Model):
    computer = models.CharField(max_length=10,  null=True, blank=True) #电脑浏览数
    mobilephone = models.CharField(max_length=10,  null=True, blank=True) #手机浏览数
    def __str__(self):
        return self.computer
    
# 上传图片  设置media以显示图片
class Course(models.Model):
    image = models.ImageField(default='', upload_to='org/%Y/%m', verbose_name='图片logo', max_length=100)