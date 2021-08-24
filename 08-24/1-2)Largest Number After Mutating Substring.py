# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 20:34:34 2021

@author: dla05
"""

'''
1-2)
LeetCode 1946. Largest Number After Mutating Substring
큰 수를 나타내는 문자열 num이 있다. 그리고 길이가 10인 정수 배열 change가 있다.
num[i]는 change[num[i]]로 바꿀 수 있다. 이렇게 num 일부를 바꾸거나 또는 바꾸지 않은채로 표현할 수 있는 가장 큰 수를 반환하라.
'''

def maximumNumber(self, num, change):
    ans = ""
    flag = False #이미 앞에서 single substring이 선택되었다는 표시
    for i in range(len(num)):
        if change[int(num[i])]>=int(num[i]):
            #change[num[i]]가 num[i]보다 크거나 같으면 숫자를 바꿀 수 있음
            ans+=str(change[int(num[i])])
            if change[int(num[i])]!=int(num[i]):
                flag=True #change[]와 num이 같은 경우에는 flag를 바꾸지 않음 -> 바꾸지 않기를 선택할 수도 있기 때문
        else:
            if flag:
                #앞에서 single substring이 이미 선택되었을 때 더이상 뒤를 바꾸지 않고 break
                ans+=num[i:]
                break
            else:
                #아직 single substring이 선택되지 않았을 때 바꾸지 않기를 선택하고 뒤를 탐색
                ans+=str(int(num[i]))
            
    return ans











