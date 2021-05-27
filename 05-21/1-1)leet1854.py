# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:18:08 2021

@author: dla05
"""

'''
1-1) Maximum Population Year
The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]
Return the earliest year with the maximum population.
'''

import heapq

def maximumPopulation(logs):
    """
    :type logs: List[List[int]]
    :rtype: int
    """
    logs.sort()
    popul=0
    heap=[]
    maxpop=0
    res=0
    for i in range(len(logs)):
        popul+=1
        year=logs[i][0]
        while len(heap)>0 and heap[0]<=year:
            heapq.heappop(heap)
            popul-=1
        heapq.heappush(heap, logs[i][1])
        if popul>maxpop:
            maxpop=popul
            res=year
    return res


logs = [[1950,1961],[1960,1971],[1970,1981]]
maximumPopulation(logs)
