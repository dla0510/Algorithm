# -*- coding: utf-8 -*-
"""
Created on Sat May  8 21:55:25 2021

@author: dla05
"""
'''
2-5) 쇠막대기
'''
s=input()

result=0 #잘린 쇠막대기 개수
s1=""
stack=[]
for i in range(len(s)):
    if s[i]=='(':
        stack.append(i)
    elif s[i]==')':
        if s[i-1]=='(':
            #레이저()
            stack.pop()
            result+=len(stack)

        else:
            result+=1
            stack.pop()
    
print(result)