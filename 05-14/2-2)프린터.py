# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:43:22 2021

@author: dla05
"""

'''
2-2) 프린터
중요도가 높은 문서를 먼저 인쇄하는 프린터
중요도를 나타내는 대기목록이 있고, 원하는 위치의 문서가 몇번째로 인쇄되는지 반환.
'''
from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque(priorities) #deque에 담기
    while (True):
        if d[0] == max(d): #대기목록 첫번째가 최우선순위 문서면
            d.popleft() #인쇄하고 ans++
            answer += 1
            if location == 0: #인쇄하는데 location이 0이면
                break #요청문서가 인쇄된것이므로 break
            else:
                location -= 1 #요청문서가 아니면 location--
        else: #대기목록 첫번째가 다른 문서면
            d.append(d.popleft()) #뒤로 보내기
            if location==0: #location이 0이면
                location=len(d)-1 #맨 뒤 index로 다시 할당
            else:
                location -= 1 #아니면 그냥 -1

    return answer





priorities = [2,1,3,2]
location = 2

priorities = [1,1,9,1,1]
location = 0















