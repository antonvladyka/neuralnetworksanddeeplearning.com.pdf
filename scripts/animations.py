# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:04:02 2018

@author:
"""

# chapter 3, animation 1
import math
def cost(x):    return x**2/2
def costd(x):   return x*x*(1-x)
def s(x):       return 1/(1+math.exp(-x))
def ov(w,b):    return s(w+b)
x = 1
w0 = 0.6
b0 = 0.9
eta = 0.15
w = w0
b = b0
Y = []
X = []
A = []
W = []
B = []
while x < 300:
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
plt.plot(X,Y)
plt.plot(X,A)
plt.plot(X,B)
plt.plot(X,W)

    
