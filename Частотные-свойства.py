# -*- coding: UTF-8 -*-

import numpy as np
from pylab import * 

freq,h=np.array([
    (10**2,64),
    (2*10**2,64),
    (1*10**3,64),
    (2*10**3,64),
    (1*10**4,60),
    (2*10**4,59),
    (1*10**5,54),
    (2*10**5,40),    
    ]).T
# print(freq)
# print(h)

eta=1.74*10**11
l=0.02
u=1000
v=sqrt(2*u*eta)
def hh(o):
    return 6*eta/v*2133333*np.sin(o*l/2/v)/o

print(hh(10**2))

def dFreq(freq):
    return freq*0.05*(1+50/freq)
xerr=dFreq(freq)
yerr=1
# print(xerr)
# fig, axes = plt.subplots(nrows=6, ncols=3)
# fig.tight_layout() 
# fig = plt.figure(figsize=(7,10))
# plt.subplots_adjust(left=0, bottom=0, right=10, top=1, wspace=0, hspace=0)

o=np.linspace(0.00001,2*10**11,10000)
# print(len(o), len(hh(o)))

plt.errorbar(freq, h, xerr=xerr, yerr=yerr, color='red')
plt.plot(freq,h,color='blue', lw=1,label='Экспериментальные данные')

plt.plot(o,hh(o),'--',color='black', label='Теоретическая зависимость', lw=1)

plt.axes().set_xscale("log", nonposx='clip')
grid(True)
legend(loc=0)
# axhline(y=0, color='black')
# axvline(x=0, color='black')

rc('text', usetex=True)
rc('font', family='Droid Sans')
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

xlabel(r'$f$, Гц')
ylabel(r'$h$, мм')
 
xlim(10**2-10,10**10)   
ylim(30,75)      

savefig( "img/freq-stats.png", dpi=500)
# show()

# i=0
# def lissajour_plot(n,m):

#     global i
#     T=[pi/2, pi, -pi/2]
#     if (n==5)and(m==2):
#         T=[pi, pi/4, pi/2]
#     if (n==5)and(m==3):
#         T=[-pi/2, pi, pi/2]        
#     for phase in T:
#         i+=1
#         plt.subplot(6,3,i).set_aspect(1)
#         ylim(-1.15,1.15)    
#         xlim(-1.15,1.15)        
#         plt.plot(sin(n*t-phase), cos(m*t), lw=2, color="black")
#         plt.title(r'$m/n=%s/%s$' % (m,n))
#         plt.tick_params(axis='both', which='major', labelsize=8)

# for x,y in [[1,1],[2,1],[3,1],[4,1],[5,2],[5,3]]:
#     lissajour_plot(x,y)

# plt.subplot_tool()
# 
