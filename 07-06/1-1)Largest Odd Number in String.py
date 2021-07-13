# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:32:54 2021

@author: dla05
"""
'''
1-1)
leetCode 1903. Largest Odd Number in String
주어진 string에서 가장 큰 홀수가 되는 substring 찾아서 반환하
'''
class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        idx=-1
        for i in range(len(num)):
            if int(num[i])%2==1:
                idx=i
        if idx==-1:
            return ""
        return num[:idx+1]
    
    
s="345677"
solution = Solution()
print(solution.largestOddNumber(s))
