# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 20:08:35 2021

@author: dla05
"""

'''
1-2)
leetCode 1936. Add Minimum Number of Rungs
사다리의 가로대의 높이가 주어진 배열 rungs 와 한번에 오를 수 있는 높이 dist 가 주어졌을 때, 사다리의 맨 꼭대기까지 올라가기 위해 추가로 설치해야하는 가로대의 수를 반환하라.
'''
from collections import deque
def solution(rungs, dist):
    answer=0
    pos=0
    rungs = deque(rungs)
    while rungs:
        h = rungs.popleft()
        dif=h-pos
        if dif>dist:
            answer+=dif//dist
            if dif%dist==0:
                answer-=1
        pos=h
    return answer



print(solution([1,3,5,10],2))

print(solution([3,6,8,10],3))














