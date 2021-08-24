# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 20:22:42 2021

@author: dla05
"""

'''
1-1) 
LeetCode 1945. Sum of Digits of String After Convert
소문자로 이루어진 문자열 s와 정수 k가 있다. s의 문자들을 각각 알파벳 순서에서 순서 번호로 변환한다.(a는 1, b는 2 이렇게) 
정수의 각 자리들의 합을 구하는 것이 transform이라고 했을 때 k번의 transform을 거친 후 결과를 출력하라.
아스키코드로 a~z는 97~122
'''
def getLucky(s, k):
    st = ""
    ans = 0
    for c in s:
        st+=str(ord(c)-96)
    
    for _ in range(k):
        ans = 0
        for c in st:
            ans+=int(c)
        st=str(ans)
        
    return ans

print(getLucky("iiii",1))







