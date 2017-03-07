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

get_jpg('http://asdfd.sdfsfef.656/3453.jpg sdfwfsdseqqftp://dfwerwe.sdfsf/222@ddd.jpg ljjkljhttps://sdff/2.jpg')

