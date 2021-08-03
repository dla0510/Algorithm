# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:44:23 2021

@author: dla05
"""

'''
2-3) [1차] 캐시
도시 이름을 검색해서 게시물을 가져오는 부분의 실행시간을 개선하기 위해 DB 캐시를 적용함(LRU 알고리즘). 캐시 크기에 따른 총 실행시간 측정 후 반환. 캐시 hit 1, 캐시 miss 5
'''
from collections import deque

def addRungs(cacheSize, cities):
    answer = 0
    cities = [i.lower() for i in cities]
    if cacheSize==0:
        return len(cities)*5
    
    cache = deque()
    for city in cities:
        if city in cache:
            answer+=1
            cache.remove(city)
            cache.append(city)
        else:
            answer+=5
            if len(cache)==cacheSize:
                cache.popleft()
            cache.append(city)
    return answer



print(addRungs(2,["Jeju", "Pangyo", "NewYork", "newyork"]))

print(addRungs(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))










