# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:04:02 2018

@author:
"""

# chapter 3, animation 1
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def h(x):
    return (np.sign(x)+1)/2
def step(x,s1,s2):
    return h(x-s1)-h(x-s2)
def sigma(x,w,b):
    return 1/(1+np.exp(-(w*x+b)))
[x,y] = np.meshgrid(np.linspace(0,1,501),np.linspace(0,1,501))
def s(x,s):
    return sigma(x,2000,-s*2000)
w1 = 50
b1 = -10
def f1(x,y,w1,b1,w2,b2):
    return sigma(x,w1,b1)
def f2(x,y,s1,s2):
    return step(x,s1,s2)#s(x,s1)-s(x,s2)
def f3(x,y,s1,s2):
    return step(y,s1,s2)#s(y,s1)-s(y,s2)

z = f2(x,y,0.301,0.501)+f3(x,y,0.401,0.701)

fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.view_init(-10,10)
ax.azim = 235
ax.elev = 15
ax.plot_surface(x,y,z,linewidth=0.1, antialiased=False,color='red')
#ax.plot_wireframe(x,y,z,linewidth=0.1)

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_clip_on(True)
ax.set_frame_on(False)
ax.set_zlim([0,2])
ax.set_xticks([0,1])
ax.set_yticks([0,1])
ax.set_zticks([0,1])



#plt.savefig('animation_41',dpi=300,pad_inches=0,bbox_inches=0)

    
