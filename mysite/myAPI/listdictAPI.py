# -*- coding: utf-8 -*-
'''
   ListDictAPI.py 列表字典类
   
2017.1.16
'''
    
class listdictAPI:
    def __init__(self, myList, myStr):
        self.subStrList = myList
        self.inputStr = myStr


    #判断列表MyList中所有元素,是否都包含在字符串MyStr中。是True、否False
    def isListAllInStr(self):
        return all([i in self.inputStr for i in self.subStrList])

        
    #判断列表MyList中的一个（含）以上元素是否包含在字符串MyStr中。是True、否False
    def isListInStr(self):
        '''
        >>> any(['a', 'b', 'c', 'd'])  #列表list，元素都不为空或0
        True
        >>> any(['a', 'b', '', 'd'])  #列表list，存在一个为空的元素
        True
        >>> any([0, '', False])  #列表list,元素全为0,'',false
        False
        '''       
        return any([i in self.inputStr for i in self.subStrList])
    
    #判断字符串MyStr是否包含在列表MyList中。是True、否False
    def isStrInList(self):
        return any([self.inputStr in i for i in self.subStrList])


