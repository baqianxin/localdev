import numpy as np
import tensorflow as tf
import os
import math
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
print(tf.__version__)

'''
Auth:baqianxin@163.com
Meta:TensorFlow 张量操作-基础学习1
'''

# 找最大值+ 科学计数法找最大值
a = [1, 2, 9, 2, 5, 6, 9]
b = np.argmax(a)
c = np.where(a == np.max(a))
d = [i for i, val in enumerate(a) if (val == max(a))]
print(b,"=>",a[b],'all1 =>',list(c[0]),"all2 =>",d)
a = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
b = [1, 0.1, -1, 0.9999999999999999, -1, 0.9999, 0.996]
c=[i for i, val in enumerate(b) if (val == max(b))]
d=[i for i, val in enumerate(b) if math.isclose(max(b), val, rel_tol = 1e-03)]
print(sum(a),c,d)

# 数组的运算
a=np.array([[6,2,3],[6,5,6],[7,8,9]])
## 转置
b=a.transpose()
## 行列式
b=np.linalg.det(a)
print('行列式：',b)
# 求逆-如果矩阵的行列式==0则矩阵不可逆
if(b==0):
    b='行列式为0矩阵不可逆'
else:
    b=np.linalg.inv(a)
# 矩阵的迹
b="矩阵的迹："+ str(np.trace(a))
# 矩阵的秩
b="矩阵的秩："+str(np.linalg.matrix_rank(a))

print(a,"\n=>\n",b)




#两个tensor 运算
#运算规则：element-wise。即c[i,j,..,k]=a[i,j,..,k] op b[i,j,..,k]
ts1=tf.constant(1.0,shape=[2,2])
ts2=tf.Variable(tf.random.normal([2,2]))
#以ts1和ts2为例：
#（1）加法+
ts_add1=tf.add(ts1,ts2,name=None)
ts_add2=ts1+ts2       #二者等价

#（2）减法-
ts_sub1=tf.subtract(ts1,ts2,name=None)
ts_sub2=ts1-ts2       #二者等价


#（3）乘法*
ts_mul1=tf.multiply(ts1,ts2,name=None)
ts_mul2=ts1*ts2
ts_mul3=tf.matmul(ts1,ts2)

#（4）除法/
ts_div1=tf.math.divide(ts1,ts2,name=None)
# ts_div2=tf.div(ts1,ts2,name=None)   #div 支持 broadcasting(即shape可不同)
ts_div3=ts1/ts2
#另外还有truediv(x,y) x,y类型必须一致,floor_div等。

