# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 20:35:39 2021

@author: dla05
"""

'''
2-2) 단어 변환
'''

def solution(begin, target, words):
    if words.count(target)==0:
        return 0
    
    answer = 0
    queue = [begin]

    while queue:
        temp = []
        for w1 in queue:
            if w1 == target:
                    return answer
            for i in range(len(words)-1, -1, -1):
                w2 = words[i]
                if sum([x!=y for x, y in zip(w1, w2)]) == 1:
                    temp.append(words.pop(i))
        queue = temp
        answer += 1


w=[1,2,3]
w.count(0)










