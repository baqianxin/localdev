#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import re
import sys
import jieba
import pandas as pd
import numpy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from os import path
import numpy as np
from PIL import Image
# 数据爬取模块
def get_comments():
    all_comments = ""
    fetchJSON_comment = "fetchJSON_comment9"
    for i in range(1, 2):
        url2 = str(i)
        url1c = 'https://club.jd.com/comment/productPageComments.action?callback='+fetchJSON_comment+url2+'&productId=1109759&score=0&sortType=5&page='
        url3c = '&pageSize=10&isShadowSku=0&rid=0&fold=1'
        
        finalurlc = url1c+url2+url3c
        xba = requests.get(finalurlc)
        # fetchJSON_comment98(
        print(finalurlc ,xba.text)
        sys.exit()
        data=json.loads(xba.text[20:-2])
        for j in data['comments']:
            content = j['content']
            all_comments = all_comments+content
        print(i,xba.text[0:20])
    print("finished")
    return all_comments
 
# 数据清洗处理模块
def data_clear():
    xt = get_comments()
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filedata = re.findall(pattern, xt)
    xx = ''.join(filedata)
    clear = jieba.lcut(xx)   # 切分词
    cleared = pd.DataFrame({'clear': clear})
    stopwords = pd.read_csv("chineseStopWords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'], encoding='GBK')
    cleared = cleared[~cleared.clear.isin(stopwords.stopword)]
    count_words = cleared.groupby(by=['clear'])['clear'].agg({"num": numpy.size})
    count_words = count_words.reset_index().sort_values(by=["num"], ascending=False)
    return count_words
 
#词云展示模块
def make_wordclound():
    d = path.dirname(__file__)
    msk = np.array(Image.open(path.join(d, "151.jpg")))
    word_frequence = {x[0]:x[1] for x in data_clear().head(200).values}
    wordcloud = WordCloud(font_path="ArialHB.ttc",mask=msk,background_color="#EEEEEE",max_font_size=250,width=1300,height=800)
    wordcloud = wordcloud.fit_words(word_frequence)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
 
if __name__=="__main__":
    make_wordclound()
    print("finish")