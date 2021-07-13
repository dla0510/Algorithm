# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 19:15:54 2021

@author: dla05
"""

'''
2-4)
baekjoon 11403. 경로 찾기
방향그래프 G가 주어졌을 때, 모든 정점 (i,j)에 대해서, i에서 j로 가는 경로가 있는지 없는지 구하시오.
'''
import sys

n = int(input())

path = [[1000000]*n for _ in range(n)]

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j]==1:
            path[i][j]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            path[i][j]=min(path[i][j],path[i][k]+path[k][j])
            
for row in path:
    for j in range(n):
        if row[j]==1000000:
            row[j]=0
        else:
            row[j]=1
        print(row[j], end=" ")
    print()












