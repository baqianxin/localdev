#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import datetime
import pandas as pd
import requests as rs
from bs4 import BeautifulSoup

def praseHtml():
    urlP = "http://www.lovegeek.cn/forum/forum.php?mod=viewthread&tid=10&extra=page%3D1"
    pageData = pd.read_html(
        urlP, attrs={'cellpadding': "0", 'cellspacing': "0"}, header=0)
    pageCH = pageData[1:2][0].columns.values.tolist()[0]
    print("当前文章主题 : ", pageCH[0:-6])
    dt = datetime.datetime.now()
    print(dt)

def praseHtmlBs4():
    io="http://pad.travelchina.gov.cn/zh/syxx/cpxx/xxgw.shtml"
    response = rs.get(io)
    html = response.content.decode("utf-8")
    soup = BeautifulSoup(html,'lxml')
    dataList = soup.select(".xpxxlbbox a")
    for row in dataList:
        print(row.attrs['href'])
        item = row.li.text
        print("http://pad.travelchina.gov.cn"+row.li.img['src'])
        print(item)
        

if __name__ == "__main__":
    praseHtmlBs4()
