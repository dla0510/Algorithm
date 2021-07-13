# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:36:32 2021

@author: dla05
"""

'''
2-2)
baekjoon 14502. 연구소
N*M 크기의 연구소에 바이러스가 퍼졌다. 0이라고 적힌 칸은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 바이러스는 상하좌우로 인접한 빈 칸으로 퍼져나갈 수 있다. 벽을 3개 새로 세울 수 있을 때 안전한 칸의 최대 개수를 구하시오.
'''
import collections
import copy
import itertools

class Solution(object):
    max_zone = 0
    
    def safezone(self, n, m, loc, cnt):
        zeros=[]
        virus=[]
        for i in range(n):
            for j in range(m):
                if loc[i][j] == 0:
                    zeros.append([i,j])
                elif loc[i][j] == 2:
                    virus.append([i,j])
        zero_combi = itertools.combinations(zeros, 3)
        for combi in zero_combi:
            self.bfs(n,m,virus,combi)
        return self.max_zone

    def bfs(self, n, m, virus, combi):
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        queue = collections.deque(virus)
        c = copy.deepcopy(loc)
        for a,b in combi:
            c[a][b]=1
        while(queue):
            x, y = queue.popleft()
            for i in range(4):
                ax = x+dx[i]
                ay = y+dy[i]
                if ax>=0 and ax<n and ay>=0 and ay<m and c[ax][ay]==0:
                    c[ax][ay]=2
                    queue.append([ax,ay])
        
        cnt = 0
        for l in c:
            cnt += l.count(0)
        self.max_zone=max(self.max_zone, cnt)
        return



n = 4
m = 6
loc = [[0,0,0,0,0,0], [1,0,0,0,0, 2], [1, 1, 1, 0,0, 2], [0,0,0,0,0, 2]]

solution = Solution()
print(solution.safezone(n, m, loc, 0))
        
        
        
        
'''
n, m = map(int, input().split())
loc = []
for _ in range(n):
    loc.append(list(map(int, input().split())))
'''
