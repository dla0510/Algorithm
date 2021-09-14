# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:20:01 2021

@author: dla05
"""

'''
1-2)
LeetCode 1980. Find Unique Binary String
'''

def findDifferentBinaryString(nums):
        n = len(nums)
        arr = []
        for i in range(2**n):
            st = format(i, 'b') #2진수로 바꾸기
            st = st.zfill(n) #길이 n이 되도록 앞에 0 채우기
            if st not in nums:
                arr.append(st)
        return arr[0]