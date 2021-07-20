# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 20:36:29 2021

@author: dla05
"""

'''
2-4)
baekjoon 2458. 키 순서
n명의 학생들이 있고 두 학생끼리 키를 비교한 결과 a번 학생의 키가 b번 학생의 키보다 작다면, a에서 b로 화살표를 그려서 표현하였다.
이 때 자신의 키가 몇 번째인지 알 수 있는 학생들이 모두 몇 명인지 계산하여 출력하라.
'''

n, m = map(int, input().split())
path = [[100000]*n for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    path[a-1][b-1]=1
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            path[i][j]=min(path[i][j], path[i][k]+path[k][j])

ans = 0
        
for i in range(n):
    check = [False]*n
    for j in range(n):
        if path[i][j]!=100000:
            check[j]=True
        if path[j][i]!=100000:
            check[j]=True
    if sum(check)==n-1:
        ans+=1
        
print(ans)
    


















