# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:04:02 2018

@author:
"""

# chapter 3, animation 1
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def sigma(x,w,b):
    return 1/(1+np.exp(-(w*x+b)))
[x,y] = np.meshgrid(np.linspace(0,1,1001),np.linspace(0,1,1001))

w1 = 50
b1 = -10
def f1(x,y,w1,b1,w2,b2):
    return sigma(x,w1,b1)
z = f1(x,y,w1,b1,0,0)


fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.view_init(-10,10)
ax.azim = 260
ax.elev = 15
ax.plot_surface(x,y,z,cmap='viridis')

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_clip_on(True)
ax.set_frame_on(False)
ax.set_zlim([0,1])
ax.set_xticks([0,1])
ax.set_yticks([0,1])
ax.set_zticks([0,1])



plt.savefig('animation_41',dpi=300,pad_inches=0,bbox_inches=0)

    
