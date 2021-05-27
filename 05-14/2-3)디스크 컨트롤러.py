# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:16:20 2021

@author: dla05
"""

'''
2-3)디스크 컨트롤러
여러개의 작업이 들어왔을 때 작업의 요청부터 종료까지 걸린 시간의 평균을 최소화할 수 있는 순서대로 처리하고 평균 반환(shortest job first)
'''
import heapq

def solution(jobs):
    answer = 0
    jobs.sort()  # 혹시 모르니까 들어온 순서대로 정렬
    length = len(jobs)
    heap = []
    current = 0  # 현재 시간

    while (True):
        if len(heap)==0 and len(jobs) > 0 and jobs[0][0]>=current:  # 작업중인 작업이 없고 들어올 작업이 남았으면
            current = jobs[0][0]  # 해당 작업 시작시간으로 jump

        while len(jobs) > 0 and jobs[0][0] <= current:  # 시작할 수 있는 모든작업을
            heapq.heappush(heap, [jobs[0][1], jobs[0][0]])  # 소요 시간 기준으로 heapq에 넣기
            jobs.pop(0)  # heapq에 들어간 작업 list에서 삭제

        current += heap[0][0]  # shortest job 작업
        answer += current - heap[0][1]  # 요청부터 종료까지 걸린 시간을 더한 후
        heapq.heappop(heap)  # pop
        if len(jobs) == 0 and len(heap) == 0:
            break

    answer /= length  # 평균구하기
    return int(answer)


jobs=[[0,3],[1,9],[2,6]]
print(solution(jobs))


