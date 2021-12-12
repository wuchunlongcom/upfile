# -*- coding: utf-8 -*-
from django.conf.urls import url, include
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

    url(r'^showimg/$', views.showimg, name='showimg'),
    
    url(r'^showimg2/$', views.showimg2, name='showimg2'),
    
    # url(r'^showimg2/$', IndexView.as_view(
    #     template_name = 'showimg2.html'), name='showimg2'),
    
               
    url("list/img", views.list_img, name='list_img'),
    
    url("list/html/", views.list_html, name='list_html'),
    
    url("api_upfile_save/", views.api_upfile_save, name='api_upfile_save'),  
         
    url(r'^image/upload/$', views.image_upload, name="image_upload"),   
]
