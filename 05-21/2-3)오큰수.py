# -*- coding: utf-8 -*-
"""
Created on Fri May 28 00:26:10 2021

@author: dla05
"""
'''
2-3)bj17298 오큰수
크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.
'''
l = int(input())
arr = list(map(int,input().split()))
arr.reverse()
res=[-1]*l

stack=[]
stack.append((l-1,arr.pop()))
for i in range(l-2,-1,-1):
    top = arr.pop()
    while top>stack[-1][1]:
        res[l-1-stack[-1][0]]=top
        stack.pop()
        if len(stack)==0:
            break
    stack.append([i,top])

for i in res:
    print(i,end=" ")

#다른 코딩 참고
import sys

input=sys.stdin.readline
l = int(input())
arr = list(map(int,input().split()))
res=[-1]*l

stack=[]
stack.append(0)
for i in range(1,l):
    top = arr[i]
    while stack and top>arr[stack[-1]]:
        res[stack[-1]]=top
        stack.pop()
    stack.append(i)

print(*res)
