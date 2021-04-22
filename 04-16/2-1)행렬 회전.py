# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 23:12:05 2021

@author: dla05
"""

import numpy as np

a= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)


def rotate90(a):
    n=len(a)
    b= np.empty((n,n),int)
    for i in range(n):
        b[n-1-i]=a[i]
    return b.T


def rotate180(a):
    n=len(a)
    b= np.empty((n,n),int)
    c= np.empty((n,n),int)
    for i in range(n):
        b[n-1-i] = a.T[i]
    for i in range(n):
        c[n-1-i]= b.T[i]
    return c

def rotate270(a):
    n=len(a)
    b= np.empty((n,n),int)
    c= np.empty((n,n),int)
    for i in range(n):
        b[n-1-i] = a.T[i]
    for i in range(n):
        c[n-1-i]= b.T[i]
    for i in range(n):
        b[n-1-i] = c[i]
    return b.T
    