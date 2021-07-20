# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 19:01:03 2021

@author: dla05
"""

'''
2-1)
baekjoon 1238. 파티
N개의 마을이 있고 M개의 단방향 도로들과 각 도로를 지나는데 걸리는 시간 Ti가 있다.
파티에 참석하기 위해 마을 X로 갔다 돌아오는 시간이 가장 긴 마을 학생의 소요시간을 구하라.
'''
import heapq
from collections import defaultdict

N, M, X = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])

def dijkstra(n,x,graph):
    dis = [10000000]*n
    dis[x-1]=0
    
    heap=[(0,x)]
    
    while heap:
        d, s = heapq.heappop(heap)
        for v,w in graph[s]:
            weighted_d = d+w
            if weighted_d < dis[v-1]:
                dis[v-1]=weighted_d
                heapq.heappush(heap, (weighted_d,v))
                
    return dis

#X에서 다른 정점들로 가는 거리
ans = dijkstra(N,X,graph)

for i in range(N):
    if i+1==X:
        continue
    ret = dijkstra(N,i+1,graph)
    #ret은 i에서 다른 정점들로 가는 거리
    ans[i]+=ret[X-1] #i에서 X로 가는 거리를 더함
    
print(max(ans))
        















