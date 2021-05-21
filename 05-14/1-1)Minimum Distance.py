# -*- coding: utf-8 -*-
"""
Created on Thu May 20 22:34:39 2021

@author: dla05
"""


def getMinDistance(nums, target, start):
    """
    :type nums: List[int]
    :type target: int
    :type start: int
    :rtype: int
    """
    result=10**4
    for i in range(len(nums)):
        if nums[i]==target:
            if abs(i-start)<=result:
                result=abs(i-start)
                print(result)
    return result

getMinDistance([1,1,1,1,1,1,1,1,1,1], 1, 9)