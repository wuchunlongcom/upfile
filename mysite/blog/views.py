# -*- coding: utf-8 -*-
import os
import datetime
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.generic.base import View
from django.http import JsonResponse

from .forms import UploadImageForm
from myAPI.fileAPI import MyFile, upfile_save, upfile_save_time, read_txt, write_txt
#from mysite.settings import MEDIA_ROOT

file_img = './blog/static/img'
file_html = './blog/templates/uphtml'
imgExt = ['.bmp', '.gif', '.jpg', '.pic', '.png', '.tif', '.jpeg', '.php',\
          '.BMP', '.GIF', '.JPG', '.PIC', '.PNG', '.TIF', '.JPEG', '.PHP']

htmlExt = ['.html', '.htm',\
           '.HTML', '.HTM']

# http://localhost:8000/blog/index/
def index(request):
    return  render(request, 'blog/index.html', context=locals())

# 上传单个文件。 http://localhost:8000/blog/upload/
def upload(request):  
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        upfile = request.FILES.get("upfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not upfile:
            messages.info(request, '没有选择文件！')  
            return HttpResponseRedirect('#')   
        res = upfile_save_time(file_img, upfile) # 保存上传文件，上传文件名加当前时间
        messages.info(request, res)
        return HttpResponseRedirect('/blog/list/img/')     
    return  render(request, 'blog/upload.html', context=locals())


# 上传单个html文件。 http://localhost:8000/blog/uphtml/
def uphtml(request):  
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        upfile = request.FILES.get("upfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not upfile:
            messages.info(request, '没有选择文件！')  
            return HttpResponseRedirect('/')   
        res = upfile_save(file_html, upfile) # 保存上传文件，上传文件同名会覆盖
        messages.info(request, res)
        return HttpResponseRedirect('/')     
    return  render(request, 'blog/uphtml.html', context=locals())


# 保存上传文件, 上传文件不会覆盖  http://localhost:8000/blog/api_upfile_save/
def api_upfile_save(request):
    res = 'hello!'
    if request.method == 'POST':
        upfile = request.FILES.get("upfile", None)
        res = upfile_save_time(file_img, upfile) # 保存上传文件，上传文件名加当前时间
    mylist = [{"res" : res }] 
    return JsonResponse(mylist, safe = False) 

#上传目录(支持多个目录)中的所有文件。不能上传目录(结构)，只会把目录和其子目录的文件上传而不会上传目录。 http://localhost:8000/blog/upfolder/
def upfolder(request):  
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        upimg = request.FILES.getlist("upimg", None)        #第一个目录 获取upimg文件列表
        upvideo = request.FILES.getlist("upvideo", None)    #第二个目录 获取upvideo文件列表
        
        writefile(request,upimg,'blog/static/upimg')        
        writefile(request,upvideo,'blog/static/upvideo')
    return  render(request, 'blog/upfolder.html', context=locals())

def writefile(request, upname, savepath):
    try:
        if not upname:
            messages.info(request, '没有选择目录！')  
            return HttpResponseRedirect('#')
        for file in upname:   
            position = os.path.join(savepath,str(file))
            f = open(position,'wb+')    # 打开特定的文件进行二进制的写操作        
            for chunk in file.chunks(): # 分块写入文件  
                f.write(chunk)  
            f.close()
        messages.info(request, '%s 所有文件上传成功!'%(upname))
    except Exception as ex:
        messages.info(request,str(ex))
    return HttpResponseRedirect('/')

def image_upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():            
            # 保存上传的图像文件。保存路径分别由settings.py和models.py设置
            form.save() 
            #print('request.raw_post_data======', request.raw_post_data) 
            return HttpResponseRedirect('/')
    #return HttpResponseRedirect('/')
    return render(request, 'blog/image_upload.html', context=locals())
 
  
# 图片懒加载显示图片技术  http://localhost:8000/blog/list/img/
def list_img(request):
    myfile = MyFile(file_img, imgExt)   
    list_img = myfile.toNameList() # ['blog/static/img/1.jpg', ...]
    list_img = ['%s' %i.split('/static/')[-1] for i in list_img] # ['img/1.jpg', ...]
    
    print('list_img======', list_img)
    return  render(request, 'list-img.html', context=locals())

#  http://localhost:8000/blog/list/html/
def list_html(request):
    myfile = MyFile(file_html, htmlExt)   
    list_html = myfile.toNameList() # ['/blog/templates/uphtml/1.html', ...]
    list_html = ['%s' %i.split('templates/')[-1] for i in list_html] # ['uphtml/1.html', ...]
    return  render(request, 'list-html.html', context=locals())

def show_html(request):
    cleanData = request.GET.dict()
    h = cleanData.get('h','')    
    filename = os.path.join(file_html, os.path.split(h)[1])
    txt = read_txt(filename)    
    items = txt.split('<g>')
    if len(items) > 1:
        txt1 = items[0]         
        txt = txt.split(txt1)[-1]
        txt = txt.split('</body>')[0]
    return  render(request, 'blog/show_html.html', context=locals())
