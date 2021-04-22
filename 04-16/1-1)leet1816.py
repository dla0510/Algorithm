# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 22:28:16 2021

@author: dla05
"""
#s = input()
class Solution(object):
    def truncateSentence(self, s, k):
        words = s.split(" ")
        result =""
        for i in range(k):
            if(i!=k-1):
                result+=(words[i]+" ")
            else:
                result+=(words[i])
        return result