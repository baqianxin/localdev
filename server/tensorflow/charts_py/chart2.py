import numpy as numpy
import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D

numpy.random.seed(42)

n_grids = 51 
c = n_grids/2
nf =2

x = numpy.linspace(0,1,n_grids)
y = numpy.linspace(0,1,n_grids)

X,Y =numpy.meshgrid(x,y)
# 生成0值得傅里叶谱
spectrum = numpy.zeros((n_grids,n_grids),dtype=numpy.complex)
# 生成噪音
# noise =  [numpy.complex(x,y) for x,y in numpy.random.uniform(-1,1,((x*nf+1)**2/2,2))]
noise = [numpy.complex(x,y) for x,y in numpy.random.uniform(-1,1,((2*nf+1)**2//2,2))]

# 傅里叶频谱的每一项和其共轭关于中心对称
noisy_block =numpy.concatenate((noise,[0j],numpy.conjugate(noise[::-1])))

# 将生成的频谱作为低频成分
# spectrum[c-nf:c+nf+1,c-nf:c+nf+1]  = noisy_block.reshape((2*nf+1,2*nf+1))
spectrum[int(c-nf):int(c+nf+1),int(c-nf):int(c+nf+1)] = noisy_block.reshape((2*nf+1,2*nf+1))

# 进行反傅里叶变换
Z = numpy.real(numpy.fft.ifft2(numpy.fft.ifftshift(spectrum)))
# 创建图表
fig  = pyplot.figure('3D surface & wire')
# 第一个子图，surface图
ax = fig.add_subplot(1, 2, 1, projection='3d')

# alpha定义透明度，cmap是color map
# rstride和cstride是两个方向上的采样，越小越精细，lw是线宽
ax.plot_surface(X, Y, Z, alpha=0.7, cmap='jet', rstride=1, cstride=1, lw=0)

# 第二个子图，网线图
ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3, lw=0.5)
# 允许鼠标旋转控制
Axes3D.mouse_init(ax)
pyplot.show()