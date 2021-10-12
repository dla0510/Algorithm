# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:43:06 2021

@author: dla05
"""

'''
1-2)
LeetCode 2001.Number of Pairs of Interchangeable Rectangles
'''
from math import factorial

def interchangeableRectangles(rectangles):
    result = 0
    l = len(rectangles)

    for i in range(l):
        rectangles[i]=float(rectangles[i][0])/rectangles[i][1]
    
    dic = {}
    
    for i in range(l):
        if rectangles[i] not in dic:
            dic[rectangles[i]]=1
        else:
            dic[rectangles[i]]+=1

    for key,value in dic.items():
        if value>1:
            result += factorial(value)/(factorial(value-2)*2)
    return result
    
print(interchangeableRectangles([[16,1],[13,7],[20,18],[21,15],[20,3],[18,12],[23,14],[16,14],[5,25],[3,8],[6,17],[22,10],[25,17],[8,13],[8,11],[4,14],[2,17],[9,22],[3,15],[18,1],[19,13],[26,6],[26,14],[9,10],[12,6],[24,3],[21,8],[17,6],[16,7],[8,9],[20,24],[25,26],[22,23],[4,25],[23,23],[24,8],[14,4],[10,18],[13,6],[7,6],[24,15],[16,22],[17,19],[2,16],[23,21],[15,26],[7,17],[14,7],[10,26],[9,8],[7,10],[1,1],[11,17],[4,20],[19,24],[18,24],[9,21],[20,22],[21,12],[10,23],[5,9],[2,3],[6,17],[5,20],[11,15],[7,19],[5,9],[12,13],[15,19],[3,26],[19,25],[13,6],[22,13],[18,7],[4,9],[13,24],[22,21],[21,9],[25,26],[21,20],[9,13],[10,5],[11,18],[6,20],[16,8]]))


print(interchangeableRectangles([[15,4],[21,33],[78,56],[71,33],[13,27],[39,21],[79,52],[37,3],[49,71],[67,58],[25,34],[24,12],[35,38],[53,63],[74,56],[3,29],[30,23],[9,22],[18,44],[28,7],[3,51],[45,69],[40,10],[64,14],[44,54],[5,49],[68,22],[28,35],[80,66],[45,1],[50,38],[42,73],[36,32],[5,10],[55,8],[10,40],[40,50],[55,28],[4,51],[18,22],[26,65],[33,17],[46,54],[43,59],[5,76],[14,33],[77,4],[19,5],[59,22],[21,26],[59,42],[6,11],[63,69],[26,45],[3,42],[21,58],[65,55],[69,70],[64,61],[76,25],[2,72],[43,77],[29,68],[65,33],[48,44],[35,15],[45,38],[54,73],[71,75],[28,73],[80,79],[74,42],[11,3],[35,13],[31,9],[80,24],[65,64],[22,69],[66,27],[70,29],[58,2],[39,17]]))