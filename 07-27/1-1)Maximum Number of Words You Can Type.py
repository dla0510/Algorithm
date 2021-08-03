# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:11:33 2021

@author: dla05
"""

'''
1-1)
leetCode 1935. Maximum Number of Words You Can Type
'''

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split()
        check=[True]*len(words)
        for l in brokenLetters:
            for i in range(len(words)):
                if l in words[i]:
                    check[i]=False
        return sum(check)

solution = Solution()
text = "leet code"
l = "lt"
print(solution.canBeTypedWords(text, l))







