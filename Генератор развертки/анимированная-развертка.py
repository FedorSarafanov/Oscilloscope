import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib as mpl
from math import *

n,m=1,1.01

xList=list()
yList=list()
omega_s=m*1
omega_r=n*1

T_r=2*pi/omega_r
T_s=2*pi/omega_s

T_r=round(T_r,3)
T_s=round(T_s,3)
print(T_r,T_s)
global T
T=0

# mpl.rcParams['axes.color_cycle'] = ['r', 'k', 'c']
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, T_r), ylim=(-1, 1))
line, = ax.plot([], [], '.', markersize=1.1, lw=0.2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

for tau in np.arange(0,10*T_s,0.001):
    t=round(tau,3)
    y=np.sin(omega_s*t)
    if round(t-T,3)==round(T_r,3):
        T=t
    xList.append(((t-T)))
    yList.append(y)

# animation function.  This is called sequentially
def animate(t):
    # xList.append(t)
    # yList.append(np.sin(t/2))
    # x = np.linspace(0, 2*pi, 100)
    # y = np.sin(omega_s*x)
    # print(t)
    # print(x,y)
    # line.set_data(x[0:t], y[0:t])
    line.set_data(xList[0:t*100], yList[0:t*100])
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
           frames=int(len(xList)/100), interval=0.5, blit=True, repeat=False)

plt.show()