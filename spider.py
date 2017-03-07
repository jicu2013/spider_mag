import re
import urllib
import os
import shutil
#1111

#test again!!!!!
def get_html(url):
	page = urllib.urlopen(url)
	html_content = page.read()
	return html_content

def spide_content(html_content, obj_type='jpg'):
	pattern = re.compile(
		'(?:https?|ftp)://'+
		'[\w.\-_/]+.' + obj_type
					)


	match_result = pattern.findall(html_content)
	print 'len: '+str(len(match_result))
	return match_result

def get_remote_obj(obj_url,obj_type='jpg'):
	down_dir='download'
	if os.path.exists(down_dir):
		shutil.rmtree(down_dir)
	os.makedirs(down_dir)
	index_obj = 1
	for obj_url_item in obj_url:
		urllib.urlretrieve(obj_url_item, ".\\"+down_dir+"\\"+'%s.%s' % (index_obj, obj_type))
		index_obj += 1

html = get_html("http://china.huanqiu.com/article/2017-03/10239691.html?from=bdwz")
get_remote_obj(spide_content(html, 'jpg'))
