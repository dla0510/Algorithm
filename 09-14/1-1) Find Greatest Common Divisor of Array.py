# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:11:50 2021

@author: dla05
"""

'''
1-1)
LeetCode 1979. Find Greatest Common Divisor of Array
'''

def findGCD(nums):
        x = max(nums)
        y = min(nums)
        #유클리드호제법
        while(y):
            x,y = y,x%y
        return(x)