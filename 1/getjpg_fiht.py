#!/usr/bin/python
#coding:utf-8
import re
import urllib
"""
其实，爬虫呢，就是分为三个步骤
    1.模拟浏览器发送一个请求(GET/POST/PUT etc.)，获得网页的源代码，也就是一个html5的内容，对应的python模块就是urllib，urllib2，requests etc.
    2.从上面得到的html内容中分离出自己想要的东西，这里有很多成熟的模块，但是在一开始的时候我们只要学会用re(正则表达式模块)就行了，能够完成大部分工作了
    3.固化/保存数据，也就是把上面找出来的东西做进一步处理(加入数据库？做成文件保存？)
下面我们来分析这个例子
"""
def getHtml(url): #这里就是第一个步骤，模拟浏览器请求，把html下载下来保存在html变量里面，然后return
    page = urllib.urlopen(url)
    html = page.read()
    return html 
# 普及一下语法知识,什么是函数（不讲面向对象，一个函数应该是只是完成一件事的，完成了这件事之后把这件事的执行结果反馈给调用这个方法的函数(用return执行反馈这个动作)
# 放在这里来讲，就是 调用了 getHtml()这个函数，传入的参数是那个网址，getHtml函数就请求到这个网址的内容，然后返回给调用这个函数的东西，然后main函数中的html参数接收了这个return过来的值（也就是html5源代码


def getImg(html): # 这里第二个步骤和第三个步骤我写到一起了。先是找出html中的指定的东西，然后使用urlretrieve将内容保存下来，大概就是这样了
    x = 0
    for imgurl in re.findall('SRC=(.*?) onload',html):
        urllib.urlretrieve('http://bbs.sjtu.edu.cn%s'%imgurl.strip('"'),'%s.jpg' % x)
        x+=1
if __name__=='__main__':
    html = getHtml("http://bbs.sjtu.edu.cn/bbstcon?board=LoveBridge&reid=1457491274")
    print getImg(html)
