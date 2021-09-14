# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:12:01 2021

@author: dla05
"""

'''
2-1)
baekjoon 2042. 구간 합 구하기
n개의 수가 주어져 있다.
'''

def maxCompatibilitySum(students, mentors):
    ans = 0
    l = len(students)
    men = [False]*l
    for s in students: #students
        max_s = 0
        pos = 0
        for j in range(l): #mentors
            score = 0
            
            if men[j]==True:
                continue
            
            for i in range(len(s)): #각 자릿수 비교
                if s[i]==mentors[j][i]:
                    score+=1
            if score>max_s:
                max_s=score
                pos=j
        men[j]=True
        ans+=max_s
    return ans

print(maxCompatibilitySum([[0,0],[0,0],[0,0]],[[1,1],[1,1],[1,1]]))
