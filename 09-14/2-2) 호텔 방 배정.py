# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:57:34 2021

@author: dla05
"""

'''
2-2) 호텔 방 배정

'''

def solution(k, room_number):
    answer = []
    room = [False]*(k+1)
    for n in room_number:
        if not room[n]:
            room[n]=True
            answer.append(n)
        else:
            for i in range(n+1,k+1):
                if not room[i]:
                    room[i]=True
                    answer.append(i)
                    break
    return answer

