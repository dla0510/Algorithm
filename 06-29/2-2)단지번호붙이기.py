# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 19:57:23 2021

@author: dla05
"""

'''
2-2)
baekjoon 2667. 단지번호붙이기
정사각형 모양의 지도에서 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
연결된 집의 모임인 단지를 정의하고 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하라.
'''
class Solution(object):

    def numberOfBuildings(self, m, n):
        global visited
        global num
        num=n
        visited = [[False] * n for _ in range(n)]
        res = []  # 아파트 단지별 집 수
        count = 0  # 아파트 수
        idx = 0
        pos = [0, 0]
        for i in range(n):
            for j in range(n):
                if m[i][j] == 1 and not visited[i][j]:
                    res.append(self.isConcanated(m, i, j))
        res.sort()
        print(len(res))
        for i in res:
            print(i)

    def isConcanated(self, m, i, j):
        count = 0
        stack = [(i, j)]
        while (stack):
            pos = stack.pop()
            if not visited[pos[0]][pos[1]]:
                visited[pos[0]][pos[1]] = True
                count += 1
                if pos[0]>0 and m[pos[0]-1][pos[1]] == 1:
                    stack.append((pos[0]-1,pos[1]))
                if pos[1]>0 and m[pos[0]][pos[1]-1] == 1:
                    stack.append((pos[0],pos[1]-1))
                if pos[1]<num-1 and m[pos[0]][pos[1] + 1] == 1:
                    stack.append((pos[0], pos[1] + 1))
                if pos[0]<num-1 and m[pos[0] + 1][pos[1]] == 1:
                    stack.append((pos[0] + 1, pos[1]))
        return count


n = int(input())

l = []
for i in range(n):
    l.append(list(map(int, input())))

solution = Solution()
solution.numberOfBuildings(l, n)



