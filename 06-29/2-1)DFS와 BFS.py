# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:26:56 2021

@author: dla05
"""

'''
2-1)
baekjoon 1260. DFS와 BFS
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력
'''
import sys
import collections


class Solution(object):
    def BFS(self, n, g, s):
        res = ""
        visited = [False] * n
        queue = collections.deque([s])

        while (queue):
            s = queue.popleft()
            if not visited[s-1]:
                res = res + str(s) + " "
                visited[s-1] = True
                l=[]
                for e in g:
                    if e[0] == s and not visited[e[1] - 1]:
                        l.append(e[1])
                    elif e[1] == s and not visited[e[0] - 1]:
                        l.append(e[0])
                l.sort()
                queue=queue+collections.deque(l)
        return res[:-1]

    def DFS(self, n, g, s):
        res = ""
        visited = [False] * n
        stack = [s]

        while (stack):
            s = stack.pop()
            if not visited[s-1]:
                res = res + str(s) + " "
                visited[s - 1] = True
                l=[]
                for e in g:
                    if e[0] == s and not visited[e[1] - 1]:
                        l.append(e[1])
                    elif e[1] == s and not visited[e[0] - 1]:
                        l.append(e[0])
                l.sort(reverse=True)
                stack=stack+l
        return res[:-1]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()

    g = []
    input = sys.stdin.readline
    n, m, s = map(int, input().split())
    for i in range(m):
        u, v = map(int, input().split())
        g.append((u, v))

    print(solution.DFS(n, g, s))
    print(solution.BFS(n, g, s))












