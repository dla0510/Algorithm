# -*- coding: utf-8 -*-
"""
Created on Fri May 28 01:44:29 2021

@author: dla05
"""

'''
3-1)괄호 변환
"균형잡힌 괄호 문자열" p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 "올바른 괄호 문자열"로 변환한 결과를 return 하도록 solution 함수를 완성해 주세요.

1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
'''

def solution(p):
    stack=[]
    for i in range(len(p)-1,-1,-1):
        stack.append(p[i])
    
    answer=recursive(stack)
    return answer

def recursive(stack):
        answer=''
        if len(stack)==0:
            return ''
        
        flag1=0  # '('의 개수
        flag2=0  # ')'의 개수
        tmp_stack=[]  
        # 올바른지 체크하기 위한 stack -> '('를 만나면 담고 ')'를 만나면 pop
        u=''
        while True:
            top=stack.pop()
            u+=top
            if top=='(':
                tmp_stack.append(top)
                flag1+=1
            else:
                if len(tmp_stack)>0:
                    tmp_stack.pop()
                flag2+=1  
            if flag1==flag2:
                #균형잡힌 괄호열이 되었을때
                break
            #남은 stack이 v가 됨
            
        if len(tmp_stack)>0: 
            #tmp_stack에 남아있는 (가 있음 ->올바른 괄호열이 아님
            answer+='('
            answer+=recursive(stack)
            answer+=')'
            answer+=reverse(u[1:len(u)-1]) #맨앞뒤 문자 제거 후 괄호방향 뒤집어서 붙이기
            return answer
        else:
            #올바른 괄호열임
            answer+=u
            answer+=recursive(stack)
            return answer

#괄호방향 뒤집어주는 함수
def reverse(strings):
    res=''
    r = {"(":")", ")":"("}
    for s in strings:
        res+=r[s]
    return res
    
solution("(()())()")
solution(")(")
solution("()))((()")














