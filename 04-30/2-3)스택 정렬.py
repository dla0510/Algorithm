# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:58:22 2021

@author: dla05
"""
'''
2-3) 스택 정렬 : 가장 작은 값이 위로 오도록 스택을 정렬하는 프로그램을 작성하라. 추가적으로 하나 정도의 스택은 사용해도 괜찮지만, 스택에 보관된 요소를 배열 등의 다른 자료구조로 복사할 수는 없다. 스택은 push, pop, peek, isEmpty의 네 가지 연산을 제공해야 한다.

하나씩 stack에서 s로 옮겨놓고 stack의 다음 값(5)이랑 담긴 값(10)을 비교해서 담긴 게 더 크면 그값(10)을 다시 stack으로 옮기고 다음 값(5)을 s로 담
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
    
    def peek(self):
        return self.arr[-1]
    
    def isEmpty(self):
        if len(self.arr)==0:
            return True
        else:
            return False
        
def stack_sort(stack):
    if stack.isEmpty==True:
        return
    
    s = Stack()
    flag=False 
    while(flag==False):
        flag=True
        l = stack.pop()
        o = stack.size()
        for i in range(o):
            if l<stack.peek():
                s.push(l)
                l=stack.pop()
                print('upper is smaller than lower ',s.show())
            else:
                s.push(stack.pop())
                flag=False
                print('upper is bigger than lower ',s.show())
            if i==o-1:
                s.push(l)
        for i in range(s.size()):
            stack.push(s.pop())
        print(stack.show())
    return stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(0)
stack.push(4)
stack.show()
stack_sort(stack)
stack.show()






