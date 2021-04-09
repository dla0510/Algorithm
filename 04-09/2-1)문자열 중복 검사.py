# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 21:39:08 2021

@author: dla05
"""
'''
1) 중복이 없는가 : 문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘. (자료구조를 추가로 사용하지않고 풀 수 있는 알고리즘도 고민)
'''

s = input()


# 자료구조 ver.
if(sorted(s)==sorted(list(set(s)))):
    print('True')
else:
    print('False')
'''
시간 복잡도 : O(N logN) -sort
공간 복잡도 : O(N)
'''

# non-자료구조 ver.
result = 'True'
for i in range(0,len(s)):
    if(s.count(s[i])>1):
        result = 'False'

print(result)
'''
시간 복잡도 : O(N^2)?? - for문 안에 count
공간 복잡도 : O(1)
'''