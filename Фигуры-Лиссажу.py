# -*- coding: UTF-8 -*-

import numpy as np
from pylab import * 


# fig, axes = plt.subplots(nrows=6, ncols=3)
# fig.tight_layout() 
fig = plt.figure(figsize=(7,10))
# plt.subplots_adjust(left=0, bottom=0, right=10, top=1, wspace=0, hspace=0)
t=np.linspace(0,2*pi,1000)

i=0
def lissajour_plot(n,m):

    global i
    T=[pi/2, pi, -pi/2]
    if (n==5)and(m==2):
        T=[pi, pi/4, pi/2]
    if (n==5)and(m==3):
        T=[-pi/2, pi, pi/2]        
    if (n==3)and(m==2):
        T=[pi/2, pi/4, pi]               
    for phase in T:
        i+=1
        plt.subplot(6,3,i).set_aspect(1)
        ylim(-1.15,1.15)    
        xlim(-1.15,1.15)        
        plt.plot(sin(n*t-phase), cos(m*t), lw=2, color="black")
        plt.title(r'$m/n=%s/%s$' % (m,n))
        plt.tick_params(axis='both', which='major', labelsize=8)

# for x,y in [[1,1],[2,1],[3,1],[4,1],[5,2],[5,3]]:
for x,y in [[3,2]]:#,[2,1],[3,1],[4,1],[5,2],[5,3]]:

    lissajour_plot(x,y)

plt.subplot_tool()
show()

