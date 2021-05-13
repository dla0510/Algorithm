# -*- coding: utf-8 -*-
"""
Created on Fri May 14 01:12:21 2021

@author: dla05
"""

'''
2-2)기능개발
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
'''
progresses=[93,30,55]
speeds=[1,30,5]
def solution(progresses, speeds):
    answer = []
    size = len(progresses)
    to_do=[i for i in range(size-1,-1,-1)]
    while len(to_do)>0:
        cnt=0
        for i in range(size):
            progresses[i]+=speeds[i]
            
        while progresses[to_do[-1]]>=100:
            to_do.pop()
            cnt+=1
            if len(to_do)==0:
                break
        if cnt>0:
            answer.append(cnt)
    
    return answer