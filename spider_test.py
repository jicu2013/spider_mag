import re
import urllib
import os
import shutil

def get_jpg(html):
    pattern = re.compile(
      '(?:https?|ftp)'+ '://[\w\.-_/]+.jpg'
    )
    match = pattern.findall(html)
    print 'len: ' + str(len(match))
    print match

def get_header_len(arg,arg_len):
    if(arg[0].isdigit()):
        ret1='s'
        _end = arg.find(':')
        ret2 = arg[0:_end]

    elif(arg[0]=='i'):
        ret1='i'
        _end = arg.find('e')
        ret2=arg[1:_end]

    elif(arg[0]=='d'):
        ret1='d'

    elif(arg[0]=='l'):#l4:test5:abcdee
        ret1='l'
        ret2=[]
        _begin=1
        _end = arg.find(':',_begin)
        while arg[_begin]!='e':
            _tmp_len=int(arg[_begin:_end])
            _tmp_item=arg[_end+1:_end+1+_tmp_len]
            print _tmp_item
            ret2.append(_tmp_item)
            _begin=_end+1+_tmp_len
            _end=arg.find(':',_begin)

print len('l4:test5:abcdee',15)
#print get_header_len('l4:test5:abcdee',)#15


#get_jpg('http://asdfd.sdfsfef.656/3453.jpg sdfwfsdseqqftp://dfwerwe.sdfsf/222@ddd.jpg ljjkljhttps://sdff/2.jpg')

