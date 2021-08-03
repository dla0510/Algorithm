# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:36:47 2021

@author: dla05
"""

'''
2-2) 가사 검색
가사의 단어들이 특정 키워드에 매치되는지 확인하고 키워드별 매치된 단어의 수 배열로 담아 반환
'''
#효용성 5개중 3개 실패
def solution(words, queries):
    answer = []
    for q in queries:
        cnt=0
        for w in words:
            cnt+=match(w,q)        
        answer.append(cnt)
        
    return answer

def match(word, query):
    if len(word)!=len(query):
        return 0
    for i in range(len(word)):
        if query[i]!="?" and word[i]!=query[i]:
            return 0
    return 1


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))
















