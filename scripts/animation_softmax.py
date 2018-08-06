# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 20:04:02 2018

@author:
"""

# chapter 3, animation 1
import numpy as np
import matplotlib.pyplot as plt
def softmax(z1, z2, z3, z4):
    N = len(z4)
    A = np.zeros((N,4))
    for j in range(N):
        z = np.array([z1,z2,z3,z4[j]])
        a = np.exp(z)
        A[j,] = a/np.sum(a)
    return(A)

N = 101
z1 = -1
z2 = 0
z3 = 1
z4 = np.linspace(-5,5,N)
A = softmax(z1,z2,z3,z4)
plt.figure(figsize=(10,3.5))
plt.subplot(1,2,1)
plt.plot(z4,A)
plt.xlabel('$z_4$')
plt.ylabel('$a_j$')
plt.legend(['$a_1$, $z_1$ = %g'%(z1),'$a_2$, $z_2$ = %g'%(z2),'$a_3$, $z_3$ = %g'%(z3),'$a_4$'],loc=0)
z1 = -0.5
z2 = 0
z3 = 1.5
z4 = np.linspace(-5,5,N)
A = softmax(z1,z2,z3,z4)
plt.subplot(1,2,2)
plt.plot(z4,A)
plt.xlabel('$z_4$')
plt.legend(['$a_1$, $z_1$ = %g'%(z1),'$a_2$, $z_2$ = %g'%(z2),'$a_3$, $z_3$ = %g'%(z3),'$a_4$'],loc=0)
plt.tight_layout()

plt.savefig('animation_softmax',dpi=300,pad_inches=0,bbox_inches=0)

    
