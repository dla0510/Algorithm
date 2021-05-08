# -*- coding: utf-8 -*-
"""
Created on Sat May  8 21:58:25 2021

@author: dla05
"""

record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    answer = []
    uid = {}
    for s in record:
        sp=s.split(" ")
        if sp[0]=='Enter' or sp[0]=='Change':
            uid[sp[1]]=sp[2]
            
    for s in record:
        sp=s.split(" ")
        if sp[0]=='Enter':
            answer.append(uid[sp[1]]+"님이 들어왔습니다.")
        elif sp[0]=='Leave':
            answer.append(uid[sp[1]]+"님이 나갔습니다.")
    return answer