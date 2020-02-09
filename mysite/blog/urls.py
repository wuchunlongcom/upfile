# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from blog import views
#from .views import upload_file #UserView
from django.views.static import serve 
from django.urls import path,include,re_path
from django.views.generic import TemplateView, ListView, View
class IndexView(TemplateView):
    template_name = 'showimg.html'


urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^upload/$', views.upload, name="upload"),
    url(r'^upfolder/$', views.upfolder, name="upfolder"),
    
    #用户图像上传
    #url("image/upload/", UserView.as_view(), name='image_upload'), 
    url("image/upload/", views.upload_file, name='image_upload'),
     
    url(r'^showimg/$', IndexView.as_view(), name="showimg"),
     
    # 图片懒加载技术 http://localhost:8000/blog/showSlackerimg/  
    url(r'^showslackerimg/$', IndexView.as_view(template_name='show-Slackerimg.html'), name="showslackerimg"),     

    url(r'^imglist/$', views.imglist, name="imglist"),
]
