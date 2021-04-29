# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 19:41:53 2021

@author: dla05
"""

def arraySign(self, nums):
    result = 0
    cnt = 0
    for i in nums:
        if(i==0): return result
        elif(i<0): cnt+=1
        
    if(cnt%2==1): 
        result = -1
    else:
        result = 1
    return result