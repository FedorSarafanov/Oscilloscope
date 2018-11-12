# -*- coding: UTF-8 -*-

import numpy as np


freq=np.array([
    # (50,40,8),  
    # (50,45,4),
    # (50,55,4),
    # (50,60,7),  
    # (50,65,9),

    # (100,75,9),
    # (100,80,7),
    # (100,85,5),
    # (100,90,3.5),
    # (100,95,2),         
    # (100,105,3),
    # (100,110,5),
    # (100,115,7),
    # (100,120,8),
    # (100,125,10),

    # (150,110,10),    
    # (150,115,9),
    # (150,120,7),
    # (150,125,6),
    # (150,130,4.5),
    # (150,135,3.5),
    # (150,140,2.5),
    # (150,145,1.5),
    # (150,155,2),
    # (150,160,3),
    # (150,165,4),
    # (150,170,4.5),
    # (150,175,5),
    # (150,180,6),
    # (150,185,6.5),
    # (150,190,7),

    # (10000,11000,3.5),
    # (10000,10500,2),
    # (10000,11500,4.5),
    # (10000,12000,5.5),
    # (10000,12500,6.5),         
    # (10000,13000,7),
    # (10000,13500,7.5),
    # (10000,14000,8),
    # # (10000,16000,10),
    # (10000,9500,4),
    # (10000,9300,5),
    (1000,1050,3),
    (1000,1100,4),
    (1000,1150,5),
    (1000,1200,6),
    (1000,1250,7),         
    (1000,1300,8),
    (1000,1350,9),
    (1000,1400,10),
    # (10000,16000,10),
    (1000,950,3),
    (1000,900,5),
    ])

sw,sig,lock=freq.T

# x=lock
# y=(sig-sw)/sw

# spl = UnivariateSpline(x, y)
# f2 = interp1d(x, y, kind='cubic')
# spl.set_smoothing_factor(0.01)

# plot(x, f2(x), '^', lw=3)
# plot(x, y, 'o', color="red", lw=3)

# grid(c='#cccccc',ls='-')

# axhline(y=0, color='black')
# axvline(x=0, color='black')
# # ylim(0,25)
# rc('text', usetex=True)
# rc('font', family='Droid Sans')
# rc('font', size=15)
# rc('text.latex',unicode=True)
# rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
# rc('text.latex',preamble=r'\usepackage[russian]{babel}')

# ylabel(r'$\frac{\nu_\text{с}-\nu_\text{р}}{\nu_\text{р}}$')
# xlabel(r'Амплоитуда синхронизации')

from math import *

dA=0.25
def dFreq(freq):
    return 0.02*(2+50/abs(freq))

def df(sweep_freq,signal_freq,locking_A):
    ddf=(dFreq(sweep_freq)+dFreq(signal_freq))/abs(signal_freq - sweep_freq)+dA/locking_A
    print(dA/locking_A)
    eff_freq=abs(signal_freq - sweep_freq)/ sweep_freq
    # print(eff_freq,abs(eff_freq)*ddf)
    return(eff_freq*ddf)

fout = open("experience/table_1k_points.out", "wt")
# fout2 = open("sin2.table", "wt")

for point in freq:
    sweep_freq=point[0]
    signal_freq=point[1]
    locking_A=point[2]
    eff_freq=(signal_freq - sweep_freq)/ sweep_freq
    if sweep_freq==50:
        clr="black"
        mrk="o"
    if sweep_freq==150:
        clr="red"
        mrk="o"
    if sweep_freq==100:
        clr="blue"
        mrk="o"            
    Scale=1/1.5
    x=locking_A/Scale
    x_l=(locking_A-dA)/Scale
    x_r=(locking_A+dA)/Scale
    y=eff_freq*20/Scale
    y_t=(eff_freq+df(sweep_freq,signal_freq,locking_A))*20/Scale
    y_b=(eff_freq-df(sweep_freq,signal_freq,locking_A))*20/Scale
    # print( r"\draw[pattern=north west lines, pattern color=%s] (%.4f,%.4f) rectangle (%.4f,%.4f);" % ("blue", x_l,y_b, x_r, y_t)  ,end="\n", file=fout)
    # print( r"\filldraw[%s] (%.4f,%.4f) circle(\Radius);" % ("\Color", x, y)  ,end="\n", file=fout)
    # print( r"%% \filldraw[black] (%.4f,%.4f) circle(0.03);" % (locking_A, eff_freq)  ,end="\n", file=fout)
    
    print(r"    (%.4f, %.4f) --" % (x, y) ,end="\n", file=fout)
    # print("%.4f %.4f" % (locking_A/2, eff_freq*5) ,end="\n", file=fout2)
    # print( r"\filldraw[%s] (%.4f,%.4f) circle(0.03);" % (clr, locking_A*1.5/Scale, eff_freq*20*1.5/Scale)  ,end="\n")


    # plot( locking_A, eff_freq, marker=mrk, color=clr, linewidth = 0.5)
# fout.close()
# fout2.close()
# print(freq[0][])

# h=np.array([50,60,70,80,90])

# m1_tkv=((m1_t1+m1_t2+m1_t3)/3)
# # print((m1_t1+m1_t2+m1_t3)/3)
# m2_tkv=((m2_t1+m2_t2+m2_t3)/3)
# # print((m2_t1+m2_t2+m2_t3)/3)
# m3_tkv=((m3_t1+m3_t2+m3_t3)/3)
# # print((m3_t1+m3_t2+m3_t3)/3)
# # a=get_A(t)

# m1_t0=(1.5+1.48+1.51)/3
# m2_t0=(1.09+1.09+1.09)/3
# m3_t0=(1.53+1.49+1.48)/3

# m1_tkv=m1_tkv-m1_t0
# # print(m1_tkv)
# m2_tkv=m2_tkv-m2_t0
# # print(m2_tkv)
# m3_tkv=m3_tkv-m3_t0
# # print(m3_tkv)
# dm1=m2_tkv[0]-m1_tkv[0]
# dm2=m3_tkv[0]-m1_tkv[0]
# m2_tkv=m1_tkv+dm1
# m3_tkv=m1_tkv+dm2

# def kvadrat_err(txt,arr):
#     dh=0.5
#     dt=0.01
#     i=0
#     for counter in h:
#         gca().add_patch(Rectangle((h[i]-dh,arr[i]-dt), 2*dh, 2*dt, color="black"))
#         print(h[i]-dh,arr[i]-dt)
#         print(txt,': h=',h[i],' t=',arr[i],' dH=0.5 ','dt=0.01')
#         print('')
#         i+=1

# kvadrat_err('m1',m1_tkv)
# kvadrat_err('m2',m2_tkv)
# kvadrat_err('m3',m3_tkv)
# # print(m1_tkv)

# # График прямой, полученной методом экстраполяции
# # x=np.arange(-10,60,0.01)

# x=np.arange(0,100,0.1)
# func = UnivariateSpline( h, m1_tkv, k=1 )
# y = func(x)
# plot( x, y, "-", color='black')


# # x=np.arange(0,100,0.1)
# func = UnivariateSpline( h, m2_tkv, k=1 )
# y = func(x)
# plot( x, y, "-", color='red')

# # x=np.arange(0,100,0.1)
# func = UnivariateSpline( h, m3_tkv, k=1 )
# y = func(x)
# plot( x, y, "-", color='green')

# # График прямой, полученной эмперически
# # x=np.arange(0,50,0.01)
# # b=5.70
# # k=1.123
# # y=x*k-b
# ylim(1,3.5)
# xlim(45,95)
# # plot( x, y, "-", color='red', linewidth = 0.3)


# # График экспериментальных точек
# # print(h)
# # plot( h, m1_tkv, marker = 's', linestyle = '--', color='black', label='m=15.7 грамм')
# # plot( h, m3_tkv, marker = 's', linestyle = '--', color='green',label='m=15.8 грамм')
# # plot( h, m2_tkv, marker = 's', linestyle = '--', color='red', label='m=23.7 грамм')


# legend(loc = 2)
# # xticks([0,10,40,50,80,90,100])
# # for TT in t:
# #     print(get_A_err(TT))

# # dm=0.05
# # i=0
# # for counter in delta_m:
# #     gca().add_patch(Rectangle((delta_m[i]-dm,a[i]-get_A_err(t[i])), 2*dm, 2*get_A_err(t[i]), color="black",fill="black"))
# #     i+=1


# # Вывод графика

# grid(True)

# axhline(y=0, color='black')
# axvline(x=0, color='black')

# rc('text', usetex=True)
# rc('font', family='Droid Sans')
# rc('font', size=15)
# rc('text.latex',unicode=True)
# rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
# rc('text.latex',preamble=r'\usepackage[russian]{babel}')

# xlabel(r'$h(t)$, см')
# ylabel(r'$t$, $c$')

# def get_T_er_arr(T):
#     tt=[]
#     for t in T:
#         dT=0.01
#         tt.append(2*dT*t)
#     return tt

# savefig( "img/ex4.png", dpi=300 )
# # savefig( "img/ex4.png")
# # show()/
# # print('m1=15.7, m2=23.7, m3=15.8')
# # print('h',h)
# # print('---')
# # print('m1-t1',np.round(m1_t1,2))
# # print('m1-t2',np.round(m1_t2,2))
# # print('m1-t3',np.round(m1_t3,2))
# # print('m1-t',np.round((m1_tkv),2))
# # # print('---ERR-t^2',np.round(get_T_er_arr(m1_tkv),4))
# # print('---')
# # print('m2-t1',np.round(m2_t1,2))
# # print('m2-t2',np.round(m2_t2,2))
# # print('m2-t3',np.round(m2_t3,2))
# # print('m2-t',np.round((m2_tkv),2))
# # # print('---ERR-t^2',np.round(get_T_er_arr(m2_tkv),4))
# # print('---')
# # print('m3-t1',np.round(m3_t1,2))
# # print('m3-t2',np.round(m3_t2,2))
# # print('m3-t3',np.round(m3_t3,2))
# # print('m3-t',np.round((m3_tkv),2))
# # # print('---ERR-t^2',np.round(get_T_er_arr(m3_tkv),4))
# # print('---')
# # print('m1-t0',np.round(m1_t0,2))
# # print('m2-t0',np.round(m2_t0,2))
# # print('m3-t0',np.round(m3_t0,2))


# # savefig( "img/ex4.eps")
# show()

