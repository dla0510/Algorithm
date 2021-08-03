# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 20:32:50 2021

@author: dla05
"""

'''
1-3)
leetCode 1937. Maximum Number of Points with Cost
주어진 배열의 한 행마다 한 칸씩 선택해서 그 칸의 point를 가질 수 있음. 하지만 이번 행의 열과 다음 행에서 선택한 열 사이의 거리만큼 점수를 차감함. 얻을 수 있는 maximum points를 반환하라.
'''

def maxPoints(points):
    answer = 0
    c1=0
    c2=0
    for i in range(len(points)):
        maxi=0
        
        if i==0:
            answer+=max(points[0])
            c1=points[0].index(answer)
            continue
                
        for j in range(len(points[0])):
            point = points[i][j]-(abs(j-c1))
            if maxi<point:
                maxi=point
                c2=j
        c1=c2
        answer+=maxi
    return answer


points = [[1,5],[2,3],[4,2]]
print(maxPoints(points))

points=[[2,4,0,5,5],[0,5,4,2,5],[2,0,2,3,1],[3,0,5,5,2]]
print(maxPoints(points))












