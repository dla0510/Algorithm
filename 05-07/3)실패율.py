# -*- coding: utf-8 -*-
"""
Created on Fri May 14 00:22:34 2021

@author: dla05
"""

'''
3)실패율
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

딕셔너리로 완성해보기
key=operator.itemgetter(1)
'''
N=8
stages=[1,2,3,4,5,6,7]

def solution(N, stages):
    answer = []
    table=[]#[클리어 못한 수,도달 수]
    for i in range(N):
        table.append([0,0]) 
    for i in stages:
        if i==N+1:
            for j in range(i-2,-1,-1):
                table[j][1]+=1
        else:
            table[i-1][0]+=1
            for j in range(i-1,-1,-1):
                table[j][1]+=1
    f_rate=[]
    for i in range(len(table)):
        if table[i][1]==0:
            f_rate.append([0,i+1])
        else:
            f_rate.append([table[i][0]/table[i][1],i+1])
    def insertSort(l):
        for i in range(1,len(l)):
            val=l[i]
            pos=i
            while pos>0 and l[pos-1][0]<val[0]:
                l[pos]=l[pos-1]
                pos-=1
                l[pos]=val
    insertSort(f_rate)
    for i in range(len(f_rate)):
        answer.append(f_rate[i][1])
    return answer