# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 16:14:21 2021

@author: dla05
"""

'''
1-1)
leetCode 1897. Redistribute Characters to Make All Strings Equal
문자열 배열 words가 있을 때 한 문자열에서 어떤 문자를 다른 문자열로 옮겨서 모든 문자열들을 같게 만들 수 있다면 true, 아니라면 false를 반환하라.
'''
from collections import defaultdict


class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        l=len(words)
        if l == 1:
            return True

        count = 0
        for word in words:
            count += len(word)

        length = count // l
        # 만약 모든 문자열을 같은 길이로 만들 수 없다면 false
        if count / l != length:
            return False

        dic = defaultdict(int)
        for word in words:
            for c in word:
                dic[c] += 1

        for k, v in dic.items():
            if v/l != v//l:
                return False

        return True
        
        
solution = Solution()

#1
words=["abc","aabc","bc"]
print(solution.makeEqual(words))

#2
words=["ab","a"]
print(solution.makeEqual(words))





