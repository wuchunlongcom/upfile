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
    
    url(r'^show/html/$', views.show_html, name="show_html"),
    
    url(r'^uphtml/$', views.uphtml, name="uphtml"),
    url(r'^upfolder/$', views.upfolder, name="upfolder"),

    
    
    url(r'^upfile/ajax/XMLHttpRequest1/$', IndexView.as_view(
        template_name = 'blog/upfile_ajax_XMLHttpRequest1.html'), 
        name='upfile_ajax_XMLHttpRequest1'),
    url(r'^upfile/ajax/XMLHttpRequest2/$', IndexView.as_view(
        template_name = 'blog/upfile_ajax_XMLHttpRequest2.html'), 
        name='upfile_ajax_XMLHttpRequest2'),
    url(r'^upfile/ajax/XMLHttpRequest3/$', IndexView.as_view(
        template_name = 'blog/upfile_ajax_XMLHttpRequest3.html'), 
        name='upfile_ajax_XMLHttpRequest3'),

    url(r'^showimg/$', IndexView.as_view(), name='showimg'),
    url(r'^showimg2/$', IndexView.as_view(
        template_name = 'showimg2.html'), name='showimg2'),
    
    
    #用户图像上传
    #from .views import upload_file #UserView
    #url("image/upload/", UserView.as_view(), name='image_upload'),  api_upfile_save
    url("image/upload/", views.image_upload, name='image_upload'),
           
    url("list/img", views.list_img, name='list_img'),
    url("list/html/", views.list_html, name='list_html'),
    
    url("api_upfile_save/", views.api_upfile_save, name='api_upfile_save'),  
         
]
