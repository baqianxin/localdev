import numpy as np
'''
a = ['this','is','a','list',"!"]

b = ['this','is','a','tuple','!']
c = {'this':'is', 'an':'unordered','dict':'!'}


for x in a:
    print(x)

for x in b:
    print(x)

for x in c:
    print(x)

for key in c:
    print(key)
'''

a = np.arange(24).reshape((2, 3, 4))

print(a[1])

u = a[1].transpose()

print(u)

z = np.roll(u, -1, axis=0)

print(z)

am=np.mean(z[0])
print(am)