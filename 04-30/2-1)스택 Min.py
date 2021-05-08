# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:47:58 2021

@author: dla05
"""
'''
2-1) 스택 Min : 기본적인 push 기능과 pop 기능이 구현된 스택에서 최솟값을 반환하는 min 함수를 추가하려고 한다. 어떻게 설계할 수 있겠는가? push, pop, min 연산은 모두 O(1) 시간에 동작해야 한다.
'''

class Stack(object):
    
    def __init__(self):
        self.arr=[]
        
    def push(self, int):
        self.arr.append(int)
        
    def pop(self):
        self.arr.pop()
        
    def size(self):
        print(len(self.arr))
        
    def min(self):
        self.arr.