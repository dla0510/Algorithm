# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:50:03 2021

@author: dla05
"""
'''
순열 확인 : 문자열 두 개가 주어졌을 때 이 둘이 서로 순열 관계에 있는지 확인하는 메서드를 작성하라.
'''

s1,s2 = map(str, input().split())

result = 'True'

if(len(s1)!=len(s2)):
    result = 'False'
else:
    for i in s1:
        if(s1.count(i)!=s2.count(i)):
            result = 'False'
        
print(result)

'''
시간복잡도 : O(n^2)?? - for문 안에 count
공간복잡도 : O(1)
'''
            
            
            
        
            
    








