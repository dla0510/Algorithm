# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 19:52:26 2021

@author: dla05
"""

'''
2-2)
baekjoon 1504. 특정한 최단 경로
N개의 정점, E개의 양방향 간선이 주어진 그래프가 있다. 1번에서 N번까지 이동 중 주어진 두 정점을 반드시 거치는 최단 경로의 길이를 출력하라.
'''
import heapq

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])

a,b = map(int,input().split())

def dijkstra(n, s, graph):
    dis=[1000000]*n
    dis[s-1]=0
    pred=[-1]*n
    
    heap=[(0,s)]
    while heap:
        d,s = heapq.heappop(heap)
        for v,w in graph[s]:
            weighted_d = d+w
            if weighted_d < dis[v-1]:
                dis[v-1]=weighted_d
                heapq.heappush(heap, (weighted_d,v))
                
    return dis
        
ret = dijkstra(N, 1, graph)
a_ret = dijkstra(N, a, graph)
b_ret = dijkstra(N, b, graph)

v1 = ret[a-1]+a_ret[b-1]+b_ret[N-1]
v2 = ret[b-1]+b_ret[a-1]+a_ret[N-1]
ans = min(v1,v2)

if ans>=1000000:
    print(-1)
else:
    print(ans)














