# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 03:04:47 2021

@author: dla05
"""

'''
bj1068)트리
'''
import sys
from collections import deque



#n = int(sys.stdin.readline())
#l = list(map(int,sys.stdin.readline().split()))
#d = int(sys.stdin.readline())
n=4
l=[-1,0,1,2]
d=2 #삭제할 노드의 index
 
queue=deque() #삭제할 노드의 index을 담을 큐
queue.append(d)

while len(queue)>0:
    d=queue.popleft() #queue에서 pop
    l[d]=-2 #삭제된 노드는 -2
    for i, value in enumerate(l):
        if value == d: #삭제할 노드를 부모노드로 가지고 있으면
            queue.append(i) #같이 삭제- queue에 index 담기

count=0
for i in range(len(l)):
    if l[i]!=-2 and i not in l: #리스트에서 값이 -2이가 아니고 자신의 index를 부모노드로 갖는 노드가 없으면
        count+=1 #count++
print(count)
