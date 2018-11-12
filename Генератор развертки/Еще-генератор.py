import matplotlib.pyplot as plt
# from drawnow import drawnow
import numpy as np
from math import *
def makeFig():
    plt.scatter(xList,yList) # I think you meant this

# plt.ion() # enable interactivity
# fig=plt.figure() # make a figure

xList=list()
yList=list()

# n,m=1,2
# n,m=2,1
# n,m=1,1
n,m=3,4
# n,m=5,2

freq_scale=100
U=1000

omega_r=n*1
omega_s=m*1

T_r=2*pi/omega_r
T_s=2*pi/omega_s

T_r=round(T_r,3)
T_s=round(T_s,3)
print(T_r,T_s)
T=0
for t in np.arange(0,18*T_s,0.001):
    b=round(t,3)
    y=U*np.sin(omega_s*b)
    # print(b-T, T_r)
    if round(b-T,3)==round(T_r,3):
        T=b
    #     # print('((((')
    # if b-T in np.linspace(0,500*T_r,501):
    #     T=b

    xList.append(((b-T))/freq_scale)
    yList.append(y)

plt.xlim(0,T_r/freq_scale)
plt.ylim(-1.1*U,1.1*U)
plt.plot(xList,yList,'.', markersize=1.5)
plt.show()