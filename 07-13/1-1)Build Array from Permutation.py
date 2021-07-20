# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 19:11:04 2021

@author: dla05
"""

'''
1-1)
leetcode 1920. Build Array from Permutation
배열 nums와 같은 길이의 배열 ans가 있을 때 모든 인덱스 i에 대해 ans[i] = nums[nums[i]] 가 되는 ans를 구하라.
'''

class Solution(object):
    def buildArray(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

nums = [0,2,1,5,3,4]
solution = Solution()
print(solution.buildArray(nums))


nums = [5,0,1,2,3,4]
solution = Solution()
print(solution.buildArray(nums))







