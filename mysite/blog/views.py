# -*- coding: utf-8 -*-
import os
import shutil
import datetime
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.http import JsonResponse
from .models import Course

from .forms import UploadImageForm
from myAPI.fileAPI import MyFile, upfile_save, upfile_save_time, read_txt, write_txt
from mysite.settings import BASE_DIR  #本地运行时 BASE_DIR = /Users/wuchunlong/local/upgit/upfile/mysite

IMG_PATH_STATIC = os.path.join(BASE_DIR, 'static', 'img')  # 部署后，显示图像文件目录
IMG_PATH_STATIC_COMMON = os.path.join(BASE_DIR, 'static_common', 'img')  # 本地运行时，显示图像文件目录
 
FILE_HTML = os.path.join(BASE_DIR, 'blog', 'templates', 'uphtml') 


imgExt = ['.bmp', '.gif', '.jpg', '.pic', '.png', '.tif', '.jpeg', '.php',\
          '.BMP', '.GIF', '.JPG', '.PIC', '.PNG', '.TIF', '.JPEG', '.PHP', '.webp']

htmlExt = ['.html', '.htm', '.HTML', '.HTM']

# http://localhost:8000/blog/index/
def index(request):
    src = '上传文件，上传的文件同名会覆盖！'
    print(BASE_DIR)  #/Users/wuchunlong/local/github/upfile/mysite
    return  render(request, 'blog/index.html', context=locals())

# 保存图像
def is_upfile_save(upfile):
    res = ''
    if '/Users' in BASE_DIR:  #本地运行
        res = upfile_save(upfile, IMG_PATH_STATIC_COMMON)
    else:  #部署后运行         
        res = upfile_save(upfile, IMG_PATH_STATIC)  
    return res

# 获得图像
def is_MyFil():
    list_img = []
    if '/Users' in BASE_DIR: #本地运行
        myfile = MyFile(IMG_PATH_STATIC_COMMON, imgExt)
        list_img = myfile.toNameList() # ['blog/static/img/1.jpg', ...]
        list_img = ['%s' %i.split('/static_common/')[-1] for i in list_img] # ['img/1.jpg', ...]
    else: #部署后运行
        myfile = MyFile(IMG_PATH_STATIC, imgExt)        
        list_img = myfile.toNameList() # ['blog/static/img/1.jpg', ...]
        list_img = ['%s' %i.split('/static/')[-1] for i in list_img] # ['img/1.jpg', ...]
        
    if list_img == ['']:
        list_img = []
    list_img_len = len(list_img)
    return list_img, list_img_len

# 上传单个图像文件。 http://localhost:8000/blog/upload/
def upload(request):  
    if request.method == "POST":   
        upfile = request.FILES.get("upfile", None)    
        if not upfile:
            messages.info(request, '没有选择文件！')  
            return HttpResponseRedirect('/')
        
        messages.info(request, is_upfile_save(upfile))
        return HttpResponseRedirect('/blog/list/img/')    
    return  render(request, 'blog/upload.html', context=locals())


# 上传单个html文件。 http://localhost:8000/blog/uphtml/
def uphtml(request):  
    if request.method == "POST":     
        upfile = request.FILES.get("upfile", None)     
        if not upfile:
            messages.info(request, '没有选择文件！')  
            return HttpResponseRedirect('/') 
        #  保存上传文件，上传文件同名会覆盖
        res = upfile_save(upfile, FILE_HTML)
        messages.info(request, res)

        return HttpResponseRedirect('/')     
    return  render(request, 'blog/uphtml.html', context=locals())

# api 保存上传文件  http://localhost:8000/blog/api_upfile_save/
def api_upfile_save(request):
    info = ''
    if request.method == 'POST':
        upfile = request.FILES.get("upfile", None)
        info =  is_upfile_save(upfile)
    return  JsonResponse({"info" : info })   
 
#上传目录(支持多个目录)中的所有文件。不能上传目录(结构)，只会把目录和其子目录的文件上传而不会上传目录。 
#http://localhost:8000/blog/upfolder/
def upfolder(request):  
    if request.method == "POST":
        res = 0
        upfiles = request.FILES.getlist("upfiles", None)    # 获取upimg文件列表
        
        for upfile in upfiles:
            is_upfile_save(upfile)         
            res += 1
            
        messages.info(request, '上传%s个文件' %res)
    return  render(request, 'blog/upfolder.html', context=locals())
 
  
# 显示4张   图片懒加载显示图片技术  http://localhost:8000/blog/list/img/
def list_img(request):
    list_img, list_img_len = is_MyFil()
    return  render(request, 'list-img.html', context=locals())

# 显示1张
def showimg(request):
    list_img, list_img_len = is_MyFil()
    return  render(request, 'showimg.html', context=locals())

# 显示2张
def showimg2(request):
    list_img, list_img_len = is_MyFil()
    return  render(request, 'showimg2.html', context=locals())

#  http://localhost:8000/blog/list/html/
def list_html(request):
    myfile = MyFile(FILE_HTML, htmlExt)   
    list_html = myfile.toNameList() # ['/blog/templates/uphtml/1.html', ...]
    list_html = ['%s' %i.split('templates/')[-1] for i in list_html] # ['uphtml/1.html', ...]    
    return  render(request, 'list-html.html', context=locals())

def show_html(request):
    cleanData = request.GET.dict()    
    htm = cleanData.get('htm','') 
    filename = os.path.join(FILE_HTML, os.path.split(htm)[1])
    txt = read_txt(filename)    
    return  render(request, 'blog/show_html.html', context=locals())

# 数据库上传图像
def image_upload(request):
    """  这是一个含数据库、form 的上传图像文件的实例 """
    imageURL = ""
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():            
            # 保存上传的图像文件。保存路径分别由settings.py和models.py设置
            form.save() 
    #获得数据库最后一条记录的image
    if Course.objects.filter().count():                    
        imageURL = Course.objects.filter(id=Course.objects.filter().last().id).first().image
    #图片验证文件在： js/plugins/jquery.upload1.js
    return render(request, 'blog/image_upload.html', context=locals())

# 数据库显示图像
def show_db_image(request):
    list_img = Course.objects.values_list('image', flat=True)
    list_img_len = len(list_img)
    return render(request, 'blog/list-image.html', context=locals())

