# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:44:33 2021

@author: dla05
"""

'''
2-3)
baekjoon 2606. 바이러스
한 컴퓨터가 웜 바이러스에 걸리면 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸린다.
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터 수를 출력하라.
'''
import collections

class Solution(object):
    def BFS(self, n, g):
        res = 0
        visited = [False] * n
        queue = collections.deque([1])

        while (queue):
            s = queue.popleft()
            if not visited[s-1]:
                res +=1
                visited[s-1] = True
                for e in g:
                    if e[0] == s:
                        queue.append(e[1])
                    elif e[1] == s:
                        queue.append(e[0])
        return res-1

    def DFS(self, n, g):
        res = 0
        visited = [False] * n
        stack = [1]

        while (stack):
            s = stack.pop()
            if not visited[s-1]:
                res += 1
                visited[s - 1] = True
                for e in g:
                    if e[0] == s:
                        stack.append(e[1])
                    elif e[1] == s:
                        stack.append(e[0])
        return res-1






if __name__ == '__main__':
    solution = Solution()

    g = []
    n = int(input())
    m = int(input())
    for i in range(m):
        u, v = map(int, input().split())
        g.append((u, v))

    print(solution.DFS(n, g))
    print(solution.BFS(n, g))
