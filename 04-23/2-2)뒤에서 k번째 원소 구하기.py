# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:13:10 2021

@author: dla05
"""

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
    
    #뒤에서 k번째 원소 구하기
    def get_fromback(self, k):
        if(k>self.size): 
            return
        else:
            index = self.size-k
            node = self.head
            i=0
            while(i<index):
                i+=1
                node=node.next
            return node.val
        
obj = MyLinkedList()
obj.addAtHead(5)
obj.addAtHead(4)
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(1)
obj.addAtHead(0)
        
