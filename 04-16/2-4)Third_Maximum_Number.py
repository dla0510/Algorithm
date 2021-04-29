# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:27:57 2021

@author: dla05
"""

nums = [1,3,10,8,8,10]
nums = [3,2,1]

def Third_Max(nums):
    num_s = sorted(nums)
    num_s.reverse()
    pos = 2
    result=0
    n=len(nums)
    if n<3:
        return num_s[0]
    for i in range(1,len(nums)):
        if num_s[i]==num_s[i-1]:
            pos+=1
        if i==pos:
            result = num_s[i]
    if pos>(len(nums)-1):
        result = num_s[0]
    return result

def Third_Max2(nums):
    num_s = sorted(list(set(nums)),reverse=True)
    if len(num_s)<3:
        return num_s[0]
    else :
        return num_s[2]