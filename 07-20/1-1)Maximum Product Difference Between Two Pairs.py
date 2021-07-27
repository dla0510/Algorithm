# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:33:52 2021

@author: dla05
"""

'''
1-1)
leetCode 1913.Maximum Product Difference Between Two Pairs
주어진 배열 nums에서 (nums[w]*nums[x] - nums[y]*nums[z])의 값이 최대가 되는 네 개의 인덱스 w,x,y,z를 찾은 후 계산되는 최대값을 출력하라.
'''
import heapq

class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        return nums[-1]*nums[-2]-nums[0]*nums[1]
         


solution = Solution()
print(solution.maxProductDifference([4,2,5,9,7,4,8]))






