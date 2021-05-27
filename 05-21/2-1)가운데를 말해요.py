# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:11:02 2021

@author: dla05
"""

'''
2-1) bj1655 가운데를 말해요
수빈이가 외치는 수가 주어졌을 때, 동샛ㅇ은 지금까지 수빈이가 말한 수 중에서 중간값을 말해야 한다.
'''
import heapq
import sys

n = int(input())
maxheap = []
minheap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if len(maxheap)==len(minheap):
        heapq.heappush(maxheap,(-num,num))
    else:
        heapq.heappush(minheap,num)

    if minheap and maxheap[0][1]>minheap[0]:
        tempmax = heapq.heappop(maxheap)
        tempmin = heapq.heappop(minheap)
        heapq.heappush(minheap,tempmax[1])
        heapq.heappush(maxheap,(-tempmin,tempmin))

    print(maxheap[0][1])