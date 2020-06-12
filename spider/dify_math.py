#!/usr/bin/python
# -*- coding:utf-8 -*-

from sympy import *
import math

# x = symbols("x")  # 符号x，自变量
# y = -pow(10, -11)*pow(x, 6) + pow(10, -8)*pow(x, 5) - 4*pow(10, -6) * \
#     pow(x, 4) + 0.0006*pow(x, 3) - 0.0428*pow(x, 2) + 1.7561*x + 16.528  # 公式


# dify = diff(y, x)  # 求导
# print(dify)  # 打印导数

# # 给定x值，求对应导数的值

# for i in range(0, 35, 1):
#     print(dify.subs('x', i), math.sin(y.subs('x', i)))
# print(math.sin(1))
# # ==========
# x, y = symbols('x, y')

# z = x**2+y**2+x*y+2
# print(z)
# result = z.subs({x: 1, y: 2})   # 用数值分别对x、y进行替换
# print(result)

# dx = diff(z, x)   # 对x求偏导
# print(dx)
# result = dx.subs({x: 1, y: 2})
# print(result)

# dy = diff(z, y)   # 对y求偏导
# print(dy)
# result = dy.subs({x: 1, y: 2})
# print(result)


class Solution:
    def minReorder(self, n, connections):
        p_allow = []
        c = 0
        hc = connections
        for k,a in hc:
            if bool(a[1] in p_allow) | a[1] == 0:
                print(p_allow)
                p_allow.append(a[0])
            if a[0] in p_allow:
                t = a[1]
                a[1] = a[0]
                a[0] = t
                c += 1
                hc.remove(a)
            else:
                continue
        print(p_allow)


sol = Solution()
sol.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
