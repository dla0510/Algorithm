# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:47:58 2021

@author: dla05
"""
'''
2-2) 스택으로 큐 : 스택 두 개로 큐 하나를 구현한 MyQueue 클래스를 구현하라.
'''

class Stack(object):
    def __init__(self):
        self.arr=[]
        
    def push(self, int):
        self.arr.append(int)
        
    def pop(self):
        return self.arr.pop()
        
    def size(self):
        return len(self.arr)
    
    def show(self):
        return self.arr

class MyQueue(object):
    def __init__(self):
        self.enqueue = Stack()
        self.dequeue = Stack()
    
    def push(self, int):
        self.enqueue.push(int)
        
    def pop(self):
        for i in range(self.enqueue.size()):
            self.dequeue.push(self.enqueue.pop())
        p = self.dequeue.pop()
        for i in range(self.dequeue.size()):
            self.enqueue.push(self.dequeue.pop())
        return p
            
    def show(self):
        return self.enqueue.show()
    
    
queue = MyQueue()
queue.push(0)
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()
queue.push(4)
queue.push(5)
queue.pop()
queue.show()


