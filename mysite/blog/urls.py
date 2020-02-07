# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views
#from .views import upload_file #UserView
from django.views.static import serve 
from django.urls import path,include,re_path


urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^upload/$', views.upload, name="upload"),
    url(r'^upfolder/$', views.upfolder, name="upfolder"),
    
    #用户图像上传
    #url("image/upload/", UserView.as_view(), name='image_upload'), 
    url("image/upload/", views.upload_file, name='image_upload'),
     
    url("showimg/", views.showimg, name='showimg'),     
]
