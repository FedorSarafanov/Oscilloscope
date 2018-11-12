import matplotlib.pyplot as plt
import numpy as np
from math import *

freq_scale=1
U=15


plt.rc('text', usetex=True)
plt.rc('font', family='Droid Sans')
plt.rc('font', size=18)
plt.rc('text.latex',unicode=True)
plt.rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
plt.rc('text.latex',preamble=r'\usepackage[russian]{babel}')

# n,m=1,2
# n,m=2,1
# n,m=1,1
# n,m=3,4
# n,m=5,2
n,m=1,0.95
# n,m=1.05,1

omega_s=m*1
omega_r=n*1

T_r=2*pi/omega_r
T_s=2*pi/omega_s

T_r=round(T_r,3)
T_s=round(T_s,3)
# print(T_r,T_s)
xList=list()
yList=list()

T=0
xList[:]=[]
yList[:]=[]
# for tau in np.arange(0,1*T_s,0.001):
for tau in np.arange(0,T_r,0.001):
    t=round(tau,3)

    y=U*np.sin(omega_s*t)

    if round(t-T,3)==round(T_r,3):
        T=t

    xList.append(((t-T))/freq_scale)
    yList.append(y)

plt.plot(xList,yList,'-', color='black', markersize=1.5, label=r'$t_1$')

xList[:]=[]
yList[:]=[]
# for tau in np.arange(0,1*T_s,0.001):
for tau in np.arange(T_r,2*T_r,0.001):
    t=round(tau,3)

    y=U*np.sin(omega_s*t)

    if round(t-T,3)==round(T_r,3):
        T=t

    xList.append(((t-T))/freq_scale)
    yList.append(y)

plt.plot(xList,yList,'--', color='red', markersize=1.5, label=r'$t_2, t_2>{t_1}$')

xList[:]=[]
yList[:]=[]
# for tau in np.arange(0,1*T_s,0.001):
for tau in np.arange(2*T_r,3*T_r,0.001):
    t=round(tau,3)

    y=U*np.sin(omega_s*t)

    if round(t-T,3)==round(T_r,3):
        T=t

    xList.append(((t-T))/freq_scale)
    yList.append(y)

plt.plot(xList,yList,'-.', color='green', markersize=1.5, label=r'$t_3, t_3>{t_2}$')
plt.legend(loc=0)
plt.grid()

# plt.axhline(y=0, color='black')
# plt.axvline(x=0, color='black')


# plt.xlabel(r'')
# plt.ylabel(r'')
plt.xlim(0,T_r/freq_scale)
plt.savefig(r'freq-%s-%s.png' % (n,m))
plt.show()