# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 23:56:58 2021

@author: dla05
"""
'''
4) 리스트의 합 : 연결리스트로 숫자를 표현할 때 각 노드가 자릿수 하나를 가리키는 방식으로 표현할 수 있다. 각 숫자는 역순으로 배열되어 있는데, 첫 번째 자리수가 리스트의 맨 앞에 위치하도록 배열된다는 뜻이다. 이와 같은 방식으로 표현된 숫자 두 개가 있을 때, 이 두 수를 더하여 그 합을 연결리스트로 반환하는 함수를 작성하라.
    입력 : (7->1->6) + (5->9->2). 즉, 617+295
    결과 : 2->1->9 즉, 912.
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    

class MyLinkedList(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(None)
        self.tail = Node(None)
        self.size = 0
        
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if (index>=self.size) : return -1
        else:
            node = self.head
            i=0
            while(i<index):
                i+=1
                node=node.next
            return node.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.next=self.head
        self.head = node
        if self.size==0 : self.tail = node
        self.size+=1
        return
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        node = Node(val)
        self.tail.next = node
        self.tail = node
        if self.size==0 : self.head = node
        self.size+=1
        return
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index>self.size :
            return
        elif index==0:
            self.addAtHead(val)
        elif index==self.size:
            self.addAtTail(val)
        else:
            i=0
            node = self.head
            while(i<index-1):
                i+=1
                node=node.next
            new = Node(val)
            new.next = node.next
            node.next = new
            self.size+=1
        return

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index>=self.size:
            return
        elif index==0:
            self.head = self.head.next
        elif index==self.size-1:
            i=0
            node = self.head
            while(i<index-1):
                i+=1
                node=node.next
            node.next = None
            self.tail=node
        else:
            i=0
            node = self.head
            while(i<index-1):
                i+=1
                node=node.next
            node.next = node.next.next
        self.size-=1
        return

#리스트의 합
def List_sum(obj1, obj2):
    size1 = obj1.size
    size2 = obj2.size
    
    s=""
    num1=0
    for i in range(size1-1,-1,-1):
        s+=str(obj1.get(i))
        num1 = int(s)
    
    s=""
    num2=0
    for i in range(size2-1,-1,-1):
        s+=str(obj2.get(i))
        num2 = int(s)
    
    s = str(num1+num2)
    
    obj = MyLinkedList()
    for i in range(len(s)):
        obj.addAtHead(int(s[i]))
    
    return obj


'''
결과 확인
'''
#List1 (7->1->6)
obj1 = MyLinkedList()
obj1.addAtHead(6)
obj1.addAtHead(1)
obj1.addAtHead(7)
#List2 (5->9->2)
obj2 = MyLinkedList()
obj2.addAtHead(2)
obj2.addAtHead(9)
obj2.addAtHead(5)

obj = List_sum(obj1,obj2)

node = obj.head
print(node.val)
while(node.next!=None):
    node=node.next
    print(node.val)
    


