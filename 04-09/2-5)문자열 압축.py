# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 19:43:07 2021

@author: dla05
"""

'''
5) 문자열 압축
반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라.
예를 들어, 문자열 aabcccccaaa 압축하면 a2b1c5a3이 된다.
만약 압축한 문자열의 길이가 기존 문자열의 길이보다 길다면 기존 문자열을 반환해야 한다.
문자열은 a-z 으로만 이루어져있다.
'''

s = input()

l = [[0 for column in range(len(s))] for row in range(2)]


pos = 0
l[0][pos] = s[0]
l[1][pos] += 1
for i in range(1,len(s)):
    if(s[i]==s[i-1]):
        l[1][pos] +=1
    else:
        pos+=1
        l[0][pos]=s[i]
        l[1][pos] += 1

count = len(l[0])-l[0].count(0)
if(count*2>len(s)):
    print(s)
else :
    result =""
    for i in range(len(l[0])):
        for j in range(len(l)):
            if(str(l[j][i])!='0'):
                result += str(l[j][i])
    print(result)

'''
시간복잡도 : O(n^2)
공간복잡도 : O(n^2)
'''







            
