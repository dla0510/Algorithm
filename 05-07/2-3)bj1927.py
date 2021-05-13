# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:56:17 2021

@author: dla05
"""

'''
2-1)bj1927 최소 힙
'''

import heapq
import sys
heap=[]

n=int(input())

for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if len(heap)==0:
            print(0)
        else:
            top=heapq.heappop(heap)
            print(top)
    else:
        heapq.heappush(heap, x)