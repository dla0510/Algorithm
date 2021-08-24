# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:21:40 2021

@author: dla05
"""

'''
2-1) 무지의 먹방 라이브
k초 후에 네트워크 장애가 발생했을 때 그 다음에 섭취해야하는 음식의 번호는?
'''
#효율성 빵점, index와 값을 담은 list로 변형해서 값으로 정렬한 후 k에서 처음 값*배열 길이를 빼면서 줄여나가
def solution(food_times, k):
    answer = 0
    
    if k>= sum(food_times):
        return -1
    l=len(food_times)
    cnt=0
    pos=0
    while(cnt<k):
        for i in range(l):
            if food_times[i]>0:
                food_times[i]=food_times[i]-1
                cnt+=1
            else:
                continue
            if cnt==k:
                pos=(i+1)%l
                break
    while food_times[pos]==0:
        pos=(pos+1)%l
    return pos+1



print(solution([3,1,2],5))









