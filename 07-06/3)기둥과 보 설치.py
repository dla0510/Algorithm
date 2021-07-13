# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 19:45:14 2021

@author: dla05
"""

'''
3) 기둥과 보 설치


'''

def solution(n, build_frame):
    answer = []
    columns=[]
    beams=[]
    for x,y,a,b in build_frame:
        if a==0: #기둥
            if b==1: #설치
                if y==0 or [x,y-1] in columns or [x-1,y] in beams or [x,y] in beams:
                    columns.append([x,y])
            else: #삭제
                if [x,y+1] not in columns and not([x,y+1] in beams and [x+1,y]):
                    columns.remove([x,y])
        else: #보
            if b==1: #설치
                if [x,y-1] in columns or [x+1,y-1] in columns or ([x-1,y] in beams and [x+1,y] in beams):
                    beams.append([x,y])
            else: #삭제
                if not ([x,y] in columns and [x-1,y] not in beams and [x,y-1] not in columns) and not([x+1,y] in columns and [x+1,y-1] not in columns [x+1,y] not in beams) and not ([x+1,y] in beams and [x+1,y-1] not in columns and [x+2,y-1] not in columns) and not ([x-1,y] in beams and [x-1,y-1] not in columns and [x-2,y-1] not in columns):
                    beams.remove([x,y])
    for i in columns:
        answer.append(i+[0])
    for i in beams:
        answer.append(i+[1])
    answer.sort()
    return answer

#print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))












