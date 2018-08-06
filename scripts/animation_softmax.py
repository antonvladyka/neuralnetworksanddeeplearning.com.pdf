# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:04:02 2018

@author:
"""

# chapter 3, animation 1
import math
def cost(x):    return -math.log(1-x)
def costd(x):   return 1/(1-x)
def s(x):       return 1/(1+math.exp(-x))
def ov(w,b):    return s(w+b)
x = 1
w0 = 2
b0 = 2
eta = 0.005
w = w0
b = b0
Y = []
X = []
A = []
W = []
B = []
while x <= 300:
    a = ov(w,b)
    d = costd(a)
    w = w - eta * d
    b = b - eta * d
    y = cost(a)
    X.append(x)
    Y.append(y)
    W.append(w)
    B.append(b)
    A.append(a)
    x = x + 1

import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.subplot(2,2,1)
plt.plot(X,Y)
plt.legend(['Cost'],loc=0)
plt.subplot(2,2,3)
plt.plot(X,A,'red')
plt.xlabel('Epoch')
plt.legend(['Output'],loc=0)
plt.subplot(2,2,2)
plt.plot(X,W,'green')
plt.legend(['Weight'],loc=0)
plt.subplot(2,2,4)
plt.plot(X,B,'black')
plt.xlabel('Epoch')
plt.legend(['Bias'],loc=0)
plt.tight_layout()
plt.savefig('animation_33',dpi=300,pad_inches=0,bbox_inches=0)
#plt.plot(X,B)
#plt.plot(X,W)

    
