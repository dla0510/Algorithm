# -*- coding: utf-8 -*-
"""
Created on Thu May 13 18:29:47 2021

@author: dla05
"""
'''
2-2)bj2493 탑
'''

#a = int(input())
#h = list(map(int,input().split( )))
a=10
h=[8,3,1,6,10,2,7,5,9,4]
res=[0]*a

stack=[]
stack.append([a-1,h.pop()])
for i in range(a-2,-1,-1):
    top=h.pop()
    while top>stack[-1][1]:
        res[stack[-1][0]]=i+1
        stack.pop()
        if len(stack)==0:
            break
    stack.append([i,top])

for i in res:
    print(i,end=" ")