# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:21:52 2021

@author: dla05
"""

def solution(board, moves):
    answer = 0
    arr = []
    n=0 #array의 크기
    p=0
    for m in moves:
        p+=1
        print(p,"번째 동작")
        for i in range(len(board)):
            if(board[i][m-1]!=0):
                arr.append(board[i][m-1])
                n+=1
                board[i][m-1]=0
                print(arr)
                break
        if n>1:
            if arr[n-1]==arr[n-2]:
                arr.pop()
                arr.pop()
                n-=2
                answer+=2
                print("pop ",arr)
    return answer

def solution(board, moves):
    answer = 0
    arr = []
    n=0
    for m in moves:
        for i in range(len(board)):
            num = board[i][m-1]
            board[i][m-1]=0
            if(num!=0):
                if (n>0) and (arr[n-1]==num):
                        answer+=2
                        arr.pop()
                        n-=1
                        break
                arr.append(num)
                n+=1
                break
    return answer

board=[[0,0,0,0,0],
       [0,0,1,0,3],
       [0,2,5,0,1],
       [4,2,4,4,2],
       [3,5,1,3,1]]

board=[[1,2,0,0,0],
       [3,4,4,0,0],
       [5,2,3,5,0],
       [1,2,0,0,0],
       [5,4,5,1,0]]
[4,3,1,1,3,2,4]

moves=[1,5,3,5,1,2,1,4]
moves=[1,5,3,5]
'''
첫번째 1
[5]
두번째 5
[5, 1]
세번째 3
[5, 1, 1] pop [5]
네번째 5
[5, 3]
다섯번째 1
[5, 3, 2]
여섯번째 2
[5, 3, 2, 3]
일곱번째 1
[5,3,2,3,1]
여덟번째 4
[5,3,2,3,1,2]
'''


solution(board,moves)







