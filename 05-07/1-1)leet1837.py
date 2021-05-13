# -*- coding: utf-8 -*-
"""
Created on Thu May 13 17:55:24 2021

@author: dla05
"""
'''
1837. Sum of Digits in Base K
n과 k가 주어졌을 때 10진수 n을 k진수로 표현한 후 각 자릿수를 더한 값을 출력해라.
'''

class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        i=0
        while int(n/k**i)>1:
            i+=1
        print(i)
        sum=0
        for i in range(i,-1,-1):
            if n>=k**i:
                p=int(n/(k**i))
                print(p)
                sum+=p
                n=n-p*(k**i)
                
        return sum