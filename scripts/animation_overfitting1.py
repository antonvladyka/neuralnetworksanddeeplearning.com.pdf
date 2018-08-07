# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:04:02 2018

@author:
"""

# chapter 3, animation 1
import numpy as np
import matplotlib.pyplot as plt
data = np.array([[ 0.7, 1.8], 
	    [ 1.3, 2.2], 
	    [ 1.9, 4.0], 
	    [ 2.6, 5.0], 
	    [ 2.9, 6.1], 
	    [ 3.6, 7.0], 
	    [ 3.8, 7.4], 
	    [ 3.95, 8.0], 
	    [ 4.4, 9.1], 
	    [ 4.9, 10.0] ])
X = data[:,0]
Y = data[:,1]
plt.figure(figsize=(6,4))
plt.scatter(X,Y)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim(0,5.5)
plt.ylim(0,11)
plt.tight_layout()
plt.savefig('animation_overfitting1',dpi=300,pad_inches=0,bbox_inches=0)

v = np.polyfit(X,Y,9)
x = np.linspace(0,5.5,55*3+1)
y = np.polyval(v,x)
plt.figure(figsize=(6,4))
plt.scatter(X,Y)
plt.plot(x,y,'black')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim(0,5.5)
plt.ylim(0,11)
plt.tight_layout()
plt.savefig('animation_overfitting2',dpi=300,pad_inches=0,bbox_inches=0)

v = np.polyfit(X,Y,1)
x = np.linspace(0,5.5,55*3+1)
y = np.polyval(v,x)
plt.figure(figsize=(6,4))
plt.scatter(X,Y)
plt.plot(x,y,'black')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.xlim(0,5.5)
plt.ylim(0,11)
plt.tight_layout()
plt.savefig('animation_overfitting3',dpi=300,pad_inches=0,bbox_inches=0)