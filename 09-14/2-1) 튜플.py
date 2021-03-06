# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:32:29 2021

@author: dla05
"""

'''
2-1) 튜플
{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}} 과 같이 집합이 주어질 때 이 집합이 어떤 튜플을 나타내는지 반환하라.
'''
import re
s="{{1,2,3},{2,1},{1,2,4,3},{2}}"


def solution(s): #{{1,2,3},{2,1},{1,2,4,3},{2}}
    ans = []
    arr = []
    s = s[1:-1] 
    #{1,2,3},{2,1},{1,2,4,3},{2}
    temp = list(re.split('},{|{|}',s)) 
    #split ['', '1,2,3', '2,1', '1,2,4,3', '2', '']
    temp = temp[1:-1] 
    #['1,2,3', '2,1', '1,2,4,3', '2']
    for i in temp:
        arr.append(list(map(int,i.split(',')))) 
        #정수 배열로 전환 [[1, 2, 3], [2, 1], [1, 2, 4, 3], [2]]
    arr.sort(key=len) 
    #길이로 정렬 [[2], [2, 1], [1, 2, 3], [1, 2, 4, 3]]
    for row in arr:
        ans+=list(set(row)-set(ans)) 
        #앞에서부터 없는 정수 차례로 더하기
    return ans
