# -*- coding: utf-8 -*-
"""
Created on Sat May  8 17:38:50 2021

@author: dla05
"""

'''
2-4)괄호의 값
    1. ‘()’ 인 괄호열의 값은 2이다.
    2. ‘[]’ 인 괄호열의 값은 3이다.
    3. ‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
    4. ‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
    5. 올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력한다. 만일 입력이 올바르지 못한 괄호열이면 0을 출력해야 한다. 
'''

#s = '(()[[]])([])'
def cal_sum(s):
    result = 0
    
    if len(s)%2!=0:
        return result
    
    stack=[]
    temp=0
    
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(ord(s[i]))
        elif s[i]=='[':
            stack.append(ord(s[i]))
        elif s[i]==')':
            flag=True
            while flag==True:
                top = stack.pop()
                if top==ord('('):
                    if temp==0:
                        stack.append(2)
                        flag=False
                    else:
                        stack.append(2*temp)
                        temp=0
                        flag=False
                elif top==ord('['):
                    return 0
                else:
                    temp+=top
                    flag=True
        elif s[i]==']':
            flag=True
            while flag==True:
                top = stack.pop()
                if top==ord('['):
                    if temp==0:
                        stack.append(3)
                        flag=False
                    else:
                        stack.append(3*temp)
                        temp=0
                        flag=False
                elif top==ord('('):
                    return 0
                else:
                    temp+=top
                    flag=True
    
    while len(stack)>0:
        top=stack.pop()
        if top==ord('(') or top==ord(')') or top==ord('[') or top==ord(']'):
            return 0
        else:
            result+=top
    return result


if __name__ == "__main__":
    s = input()
    print(cal_sum(s))









