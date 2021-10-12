# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:38:26 2021

@author: dla05
"""
'''
1-1)
LeetCode 2000.Reverse Prefix of Word
'''
def reversePrefix(word, ch):
        idx=word.find(ch)
        result = ""
        for i in range(idx,-1,-1):
            result+=word[i]
        result+=word[idx+1:]
        return result