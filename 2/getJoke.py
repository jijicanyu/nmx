#!/usr/bin/env python
#coding:utf-8
"""
  Author:  fiht --<fiht@qq.com>
  Purpose: 抓取笑话呀～
  Created: 2016年08月30日
"""
import requests
import re
#----------------------------------------------------------------------
def get_sth():
    """获取糗事百科的段子呀"""
    url = 'http://www.qiushibaike.com/text/'
    return [i.strip() for i in re.findall(re.compile('<div class="content">(.*?)</div>',re.S),requests.get(url).text)]
if __name__=='__main__':
    jokes = get_sth()
    for i in jokes: print('----\n%s\n'%i) 
    
