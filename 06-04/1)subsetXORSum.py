# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 01:06:11 2021

@author: dla05
"""

def subsetXORSum(nums):
    n = len(nums)
    sum=0
    for i in range(1<<n): # 0001,0010,0100,1000
    # i : 0000, 0001, 0010, 0011, 0100, 0101, 0110, 0111
        print('i ',i,'번째 ',1<<n)
        temp=[]
        for j in range(n): # j: 0,1,2
            t_f = i & (1 << j) # 0001, 0010, 0100,
            #i가 0000이면 false,false,false, i가 0001이면 ture,false,false, 0010이면 false,true,false, 0011이면 true,true,false, 0100이면 false,false,true,...
            if t_f: # t_f 가 0 이 아닌 경우에는 append.
                temp.append(nums[j]) # 5, 1, 6
        sum+=XORsum(temp)
    return sum

def XORsum(nums):
    if len(nums)==0: return 0
    sum=nums[0]
    for i in range(1,len(nums)):
        sum^=nums[i]
    return sum

subsetXORSum([1,3])
subsetXORSum([5,1,6])
