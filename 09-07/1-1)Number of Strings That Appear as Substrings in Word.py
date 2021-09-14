# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:57:47 2021

@author: dla05
"""

'''
1-1)
LeetCode 1967. Number of Strings That Appear as Substrings in Word
'''

def numOfStrings(patterns, word):
        res = 0
        for p in patterns:
            if p in word:
               res+=1
        return res