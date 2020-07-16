# -*- coding: utf-8 -*-

import easyocr
from PIL import ImageDraw, Image
import urllib.request as urllib
import matplotlib.pyplot as plt

url = 'http://a4.att.hudong.com/48/36/01300536763966137011362221325.jpg'
r = urllib.urlopen(url)
f = open('demo.jpg', 'wb')
f.write(r.read())
f.close()
im = Image.open("demo.jpg")
reader = easyocr.Reader(['ch_sim', 'en'])
bounds = reader.readtext('demo.jpg')
print(bounds)


def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image


draw_boxes(im, bounds)
plt.figure("Image")  # 图像窗口名称
plt.imshow(im)
plt.axis('on')  # 关掉坐标轴为 off
plt.title('image')  # 图像题目
plt.show()
