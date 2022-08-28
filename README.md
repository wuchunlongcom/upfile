### upfile 
功能：前台或后台上传单个文件

python3.7.5
上传文件, 本例使用函数upfile_save()，上传的文件同名会覆盖; 
若使用函数upfile_save_time(),上传的文件不会覆盖;                        

```
一、上传单个文件
1、上传单个文件,分别保存在(../static/img、../static_common/img)。
2、上传文件进度条、CSRF验证。     
3、批量上传文件，上传目录(支持多个目录)中的所有文件。
但是不能上传目录(结构),只会把目录和其子目录的文件上传而不会上传目录。      
4、正确使用myAPI
5、图片懒加载显示    

二、上传单个html文件,保存在(../blog/templates/uphtml)。

三、上传目录(支持多个目录)中的所有文件。不能上传目录(结构)，只会把目录和其子目录的文件上传而不会上传目录。

四、上传图像文件(数据库)。 上传图像文件，名称保存在数据库，内容保存在../media/image。 
```


```
def saveupfile(mode, filename):    
    try:
        f = open(filename, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in mode.chunks():  # 分块写入文件  
            f.write(chunk)
        f.close()
        return  filename      
    except Exception as ex:
        print("err: %s" %ex)
        return str(ex)    
 2022.08.28 重构
```