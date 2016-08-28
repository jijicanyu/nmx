#!/usr/bin/env python3

import requests
import re
import time

def get_html_source(url):
    page_re = requests.get(url)
    src = page_re.text
    return src

def get_next_html(srcern):
    rext = r'<a href="(.+?)" rel="nofollow">\n<!--<a href=".+?" rel="nofollow">-->\n<span class="next">\n下一页'
    rexter = re.compile(rext)
    urler = re.findall(rexter, srcern)
    urler.append('')
    urler = r'http://www.qiushibaike.com' + urler[0]
    return urler

def get_duanzi(srcerd):
    srcerd = re.sub(r'[\x00-\x1f]', r'', srcerd)
    redz = r'<div class="content">(.+?)</div>'
    redzer = re.compile(redz, re.S)
    duanzilist = re.findall(redzer, srcerd)
    for duanzi in duanzilist:
        duanzi = re.sub(r'<br/>', r'\n', duanzi)
        print(duanzi)
        duan.write('\n\n-+-+-+-\n{}\n-+-+-+-\n\n'.format(duanzi))
        qwer = input('\n[quit]or[q]or[退出]-退出本页\n')
        if qwer in quiter:
          break  
    return(url + '\n本页完毕')

duan = open('duanzis.text', 'a+')
duan.write('开始浏览\n' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n\n')
qwer = 'next'
quiter = ('q', 'quit', '退出')
url = input('请输入网址:')

while qwer not in quiter:
    src = get_html_source(url)
    print(url + '\n本页开始\n')
    print(get_duanzi(src))
    url = get_next_html(src)
    qwer = str(input('\n[quit]or[q]or[退出]将退出本次浏览,其他进入下一页\n'))

duan.write('结束浏览\n' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n\n')
duan.close()

print('over')

