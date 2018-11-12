# -*- coding: UTF-8 -*-

import numpy as np
from pylab import * 
from scipy.interpolate import UnivariateSpline

fout = open("experience/table_1k_points.out", "wt")

U_3,h_3=np.array([
    (3,26),  
    (3.5,30),  
    (4,34),    
    ]).T

U_4,h_4=np.array([
    (3,34),  
    (3.5,40),  
    (4,46),    
    ]).T

U_5,h_5=np.array([
    (3,44),  
    (3.5,52),  
    (4,60),    
    ]).T

U_err=2.5*0.01*5
h_err=1
hist=[r'Усиление -- 5',r'Усиление -- 4',r'Усиление -- 3']
color=['blue','black','red']
i=0
for U,H in [[U_5,h_5],[U_4,h_4],[U_3,h_3]]:
    # func = UnivariateSpline( U, H, k=1)
    func = UnivariateSpline( [0,3.5], [0, H[1]], k=1)
    x=np.linspace(0,4.5,50)
    y = func(x)
    plot( x, y, "--", color='black')    
    # plot( [0,3.5], [0, H[1]], "--", color='black')
    plt.errorbar(U,H, xerr=U_err, yerr=h_err, color='red')
    plt.plot(U,H,color=color[i], lw=1,label=hist[i])
    i+=1

# for U,H in [[U_3,h_3],[U_4,h_4],[U_5,h_5]]:
#     # print( r"\draw[pattern=north west lines, pattern color=%s] (%.4f,%.4f) rectangle (%.4f,%.4f);" % ("blue", x_l,y_b, x_r, y_t)  ,end="\n", file=fout)
#     # print( r"\filldraw[%s] (%.4f,%.4f) circle(\Radius);" % ("\Color", x, y)  ,end="\n", file=fout)
#     # print( r"%% \filldraw[black] (%.4f,%.4f) circle(0.03);" % (locking_A, eff_freq)  ,end="\n", file=fout)
    
#     print(r"    (%.4f, %.4f) --" % (x, y) ,end="\n", file=fout)
# fout.close()


grid(True)
legend(loc=0)
axhline(y=0, color='black')
axvline(x=0, color='black')

rc('text', usetex=True)
rc('font', family='Droid Sans')
rc('text.latex',unicode=True)
rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')

xlabel(r'$U$, вольт')
ylabel(r'$h$, мм')

xlim(0)   
ylim(0)        
savefig( "img/linear.png", dpi=500)

# show()