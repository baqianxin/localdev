#!/usr/bin/python

site= {'name': 'C', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print(pop_obj)
site["name"]="A"
del site["name"]
print(site)


list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print(list1)
for x in [1, 2, 3]: print(x)


# 元组元素无法修改
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])