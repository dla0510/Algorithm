# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:23:16 2021

@author: dla05
"""

'''
3)보석 쇼핑
주어진 진열대에서 모든 종류의 보석을 하나 이상 포함하는 가장 짧은 구간을 반환
'''
from collections import defaultdict
import heapq

def solution(gems):
    heap = []
    n = len(set(gems))
    find = defaultdict(int)  # 구간 안에 특정 보석이 있는지 확인

    start, end = 0, 0

    while (True):
        if len(find)<n:  # 아직 보석을 다 찾지 못했으면
            if end==len(gems):
                break
            find[gems[end]] += 1
            end += 1 #end++
        else:  # 모든 보석을 갖는 구간 [start,end]를 찾았으면
            while len(find)==n: #start를 증가시켜가며 더 짧은 구간 찾기
                heapq.heappush(heap, [end - start, start+1, end])  # push
                find[gems[start]]-=1
                if(find[gems[start]]==0):
                    del find[gems[start]]
                start += 1  # start++
                #보석 종류가 하나 빠지면 다시 end++ 구간으로 돌아감

            if heap[0][0]==n:
                #만약 모든보석을 가질 수 있는 가능한 가장 짧은 길이(보석 종류개수)의 구간을 찾았을 겨우
                break #바로 종료

    return [heap[0][1], heap[0][2]]


gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
solution(gems)
