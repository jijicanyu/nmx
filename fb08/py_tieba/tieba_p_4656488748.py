#!/usr/bin/python
#coding:utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src=\"(http://imgsrc\.bai.*?\.jpg)\"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 1000
    for imgurl in imglist:
        x = x + 1
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
    return x

html = getHtml("http://tieba.baidu.com/p/4656488748")
print getImg(html)

