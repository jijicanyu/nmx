#!/usr/bin/python
#coding:utf-8
import re
import urllib
import time

mimitext = open('mimitext.text','a+')
mimitext.write('\n' + '<<<<<<------->>>>>>' + '\n')
mimitext.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n\n')

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getMimi(html):
    reg = r'<div class=\"mimi_box\">.*?<p>(.*?)</div>'
    mimi = re.compile(reg,re.S)
    mimilist = re.findall(mimi,html)
    return mimilist

html = getHtml("http://www.umimi.cn/mimi/tag_%E7%B3%97%E4%BA%8B.html")
mimilist = getMimi(html)
p = 1000

for mimin in mimilist:
    p = p + 1
    mimin = re.sub(r'[\x00-\x1f]','',mimin)
    mimin = re.sub(r'</p><p>',r'\n',mimin)
    mimin = re.sub(r'</p>',r'\n',mimin)
    mimin = re.sub(r'\n\n',r'\n',mimin)
    mimitext.write('--%s--' % p)
    mimitext.write("\n%s\n" % mimin)

p = p - 1000
mimitext.write('<<<<<<\n>>>>>>共计%s篇' % p)
mimitext.write('\n' + '>>>>>>over<<<<<<' + '\n')
mimitext.close()

