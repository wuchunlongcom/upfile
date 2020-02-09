# -*- coding: utf-8 -*-
import os
import datetime
from .listdictAPI import  listdictAPI

class MyFile:
    """
        from myAPI.fileAPI import MyFile
        myfile = MyFile('blog/static/img/', ['.jpg'])
        imgs = myfile.toNameList()    
    """
    def __init__(self, dirpath, extlist):#extlist ＝［］获得指定目录下,全部目录名、文件名
        self.dirPath = dirpath # 目录路径 dirpath = '.../edustack/upvideo/testMyFile'
        self.extList = extlist # 指定类型的文件名列表extlist = ［'.txt'］获得全部扩展名为.txt文件名
        
    # 以列表形式，获得指定目录下，指定类型的全部文件名。extlist ＝［］获得指定目录下,全部目录名、文件名.    
    def toNameList(self):
        try:
            # 列表形式，返回指定目录下所有的文件和目录名（不含路径的短文件名）
            fileNames = os.listdir(self.dirPath)       
        except Exception as ex:
            print('Error execute: {}'.format(ex))
            # raise
            return ['']  # L1 = []与 L2 = [''] 区别：L1[0] 出错；L2[0] 不出错 2018.10.28    
        if (len(self.extList) > 0):
             fileNames = [fileName for fileName in fileNames 
                         if listdictAPI(self.extList, fileName).isListInStr()]
        filepathList = [os.path.join(self.dirPath, i) for i in fileNames 
                    if (not '._' in i)&(not '.DS' in i)] #（含路径的文件名）2016.10.24
        if filepathList == []:
            filepathList = ['']            
        return filepathList

def upfile_save(filepath, mode):
    """
    保存上传文件：上传文件名添加当前时间，上传文件不会覆盖
    """
    name, etx = os.path.splitext(mode.name)
    filename = '%s-%s%s' %(name, datetime.datetime.now().strftime('%Y%m%d[%H:%M:%S]'), etx)    
    destination = open(os.path.join(filepath, filename), 'wb+')  # 打开特定的文件进行二进制的写操作  
    for chunk in mode.chunks():  # 分块写入文件  
        destination.write(chunk)  
    destination.close() 
