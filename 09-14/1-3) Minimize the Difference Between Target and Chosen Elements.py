# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:34:41 2021

@author: dla05
"""

'''
1-3) Minimize the Difference Between Target and Chosen Elements
'''
from itertools import product

def minimizeTheDifference(mat, target):
    min_dif=100000000
    for prod in product(*mat):#행마다 하나씩 고른 모든 조합을 담은 배열
        s=sum(prod)
        dif = abs(s-target)
        if dif<min_dif:
            min_dif=dif
            if dif==0:
                return 0
    return min_dif

minimizeTheDifference(mat, 0)
    