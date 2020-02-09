# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.views.static import serve 
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from . import views

class IndexView(TemplateView):
    template_name = 'showimg.html'

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^upload/$', views.upload, name="upload"),
    url(r'^upfolder/$', views.upfolder, name="upfolder"),
    
    #用户图像上传
    #from .views import upload_file #UserView
    #url("image/upload/", UserView.as_view(), name='image_upload'),  api_upfile_save
    url("image/upload/", views.upload_file, name='image_upload'),
    
    url(r'^showimg/$', IndexView.as_view(), name='showimg'),
    url(r'^showimg2/$', IndexView.as_view(template_name = 'showimg2.html'), name='showimg2'),
    url("imglist/", views.imglist, name='imglist'),
    url("api_upfile_save/", views.api_upfile_save, name='api_upfile_save'),  
         
]
