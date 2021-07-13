# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:08:52 2021

@author: dla05
"""

'''
2-4)네트워크
컵퓨터 A와 B가 연결되어있고, B와 C가 연결되어 있을 때 컴퓨터 A와 C도 간접적으로 연결되어 정보를 교환할 수 있으므로 컴퓨터 A,B,C는 같은 네트워크 상에 있다고 할 수 있다.
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 출력하라.
'''

def solution(n, computers):
    answer = 0
    global visited
    visited = [False] * n
    
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if computers[i][j] == 1 and not visited[i] and not visited[j]:
                dfs(n, computers, i, j)
                answer+=1
    for i in visited:
        if i==False:
            answer+=1
    return answer

def dfs(n, m, i, j):
    stack = [i,j]
    while(stack):
        pos = stack.pop()
        if not visited[pos]:
            visited[pos] = True
            for p in range(n):
                if m[pos][p]==1:
                    stack.append(p)
    return


