# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:40:16 2021

@author: dla05
"""

'''
2-1)
baekjoon 1697.숨바꼭질
숨바꼭질 중인 수빈이와 동생의 위치가 N, K로 주어진다. 수빈이는 걸어서 1초에 X-1 또는 X+1로 이동하거나 순간이동으로 2*X로 이동할 수 있다. 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하시오.
'''
import collections
import math

class Solution(object):
    def hide_and_seek(self, n, k):
        dic = {}
        queue = collections.deque([n])
        dic[n]=0
        while(queue):
            n=queue.popleft()
            cur = [n+1, n-1, n*2]
            for p in cur:
                if p<0 or p>100000:
                    continue
                if p in dic:
                    continue
                queue.append(p)
                dic[p]=dic[n]+1
                if p==k:
                    break
        print(dic[k])
                
            
                
n, k = map(int,input().split())
solution = Solution()
solution.hide_and_seek(n, k)
'''
6 8 -> 2
6 9 -> 3
6 16-> 3
'''



