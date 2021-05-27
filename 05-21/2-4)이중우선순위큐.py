# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:11:23 2021

@author: dla05
"""

'''
2-4) 이중우선순위큐
이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현.

'''
import heapq


def solution(operations):
    answer = [0,0]
    heap = []
    for i in range(len(operations)):
        if operations[i][0] == 'I':
            heapq.heappush(heap, int(operations[i][2:]))

        elif operations[i][0] == 'D':
            if len(heap) == 0:
                continue

            if operations[i][2] == '1':
                heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
            else:
                heapq.heappop(heap)
    if len(heap)>0:
        answer[0]=heapq.nlargest(1, heap)[0]
        answer[1]=heap[0]
    return answer