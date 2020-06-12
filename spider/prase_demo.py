#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import datetime
import pandas as pd

def praseHtml():
    urlP = "http://www.lovegeek.cn/forum/forum.php?mod=viewthread&tid=10&extra=page%3D1"
    pageData = pd.read_html(
        urlP, attrs={'cellpadding': "0", 'cellspacing': "0"}, header=0)
    pageCH = pageData[1:2][0].columns.values.tolist()[0]
    print("当前文章主题 : ", pageCH[0:-6])
    dt = datetime.datetime.now()
    print(dt)


if __name__ == "__main__":
    praseHtml()
