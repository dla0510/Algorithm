# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 20:24:55 2021

@author: dla05
"""

'''
2-1) 가장 먼 노드
'''

from collections import deque

def solution(n, edge):
    answer = 0
    graph = {}
    visited = [False]*n
    for e in edge:
        graph[e[0]] = graph.get(e[0], [])+[e[1]] 
        #graph[e[0]]이 아무것도 없으면 [] 반환
        graph[e[1]] = graph.get(e[1], [])+[e[0]]
    queue = deque()
    queue.append(1)
    visited[0]=True
    while queue:
        nodes = len(queue)
        for i in range(nodes):
            cur = queue.popleft()
            for c in graph[cur]:
                if visited[c-1] == 0:
                    visited[c-1] = 1
                    queue.append(c)
                    
    return nodes


solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

















