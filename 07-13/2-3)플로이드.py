# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 20:18:42 2021

@author: dla05
"""

'''
2-3)
baekjoon 11404. 플로이드
n개의 도시와 각 도시들을 연결하는 m개의 버스와 각 버스별 비용이 있다.
모든 도시의 쌍 (A,B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하라.
'''
import sys

n = int(input())
m = int(input())

path = [[10000001]*(n) for _ in range(n)]
for i in range(n):
    path[i][i]=0
    
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    path[a-1][b-1] = min(path[a-1][b-1],c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            path[i][j] = min(path[i][j],path[i][k]+path[k][j])
            
for row in path:
    for j in range(n):
        if row[j]==10000001:
            row[j]=0
        print(row[j], end=" ")
    print()














