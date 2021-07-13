# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 18:17:43 2021

@author: dla05
"""

'''
2-3)
baekjoon 1753. 최단경로
V개의 정점과 E개의 간선을 갖고 있는 방향그래프가 있다. 시작점 K에서 다른 모든 정점으로의 최단 경로를 구하여라.
'''
import heapq
import sys
import collections

V, E = map(int, input().split())
s = int(input())
graph = collections.defaultdict(list)
for _ in range(E):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append([v,w])

distance=[1000000000]*V
distance[s-1]=0

queue=[[0,s]]
    
while(queue):
    dis, s = heapq.heappop(queue)
    for n,w in graph[s]:
        w_dis = dis+w
        if w_dis < distance[n-1]:
            distance[n-1] = w_dis
            heapq.heappush(queue, [w_dis, n])
            
for i in distance:
    print(i if i!=1000000000 else 'INF')











