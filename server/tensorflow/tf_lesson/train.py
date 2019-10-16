from __future__ import absolute_import, division, print_function

import tensorflow as tf
import os as os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# tf.enable_eager_execution()
tf.executing_eagerly()

x = [[2.]]
m = tf.matmul(x, x)
print("hello, {}".format(m))

a = tf.constant([[1, 2],
                 [3, 4]])
print(a)
# Broadcasting support
b = tf.add(a, 1)
print(b)
# Operator overloading is supported
# 哈达玛积
print(a * b)
# 矩阵的点积
c =  tf.matmul(a,b)
print(c)
# 验证shape参数的意义：维度/
d =  tf.constant([
    [2,2,2],
    [3,3,3]
])
e = tf.matmul(a,d)
# print(e)

# 动态流控制

def fizzbuzz(max_num):
  counter = tf.constant(0)
  max_num = tf.convert_to_tensor(max_num)
  for num in range(1, max_num.numpy()+1):
    num = tf.constant(num)
    if int(num % 3) == 0 and int(num % 5) == 0:
      print('FizzBuzz')
    elif int(num % 3) == 0:
      print('Fizz')
    elif int(num % 5) == 0:
      print('Buzz')
    else:
      print(num.numpy())
    counter += 1

# fizzbuzz(15)