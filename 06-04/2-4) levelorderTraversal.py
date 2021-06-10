# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 02:33:15 2021

@author: dla05
"""

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        queue = deque()
        if root!=None: queue.append(root)
        
        while len(queue)>0:
            l=[] #현재 레벨 node들을 담을 리스트

            for i in range(len(queue)):#현재 queue에 있는 node 전부 출력
                node=queue.popleft()
                if node.left!=None: queue.append(node.left) #node.left queue에 담기
                if node.right!=None: queue.append(node.right) #node.right queue에 담기
                l.append(node.val) #node.val list에 담기
            
            result.append(l) #result에 현재 레벨 노드들을 담은 리스트 담
            
        return result
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        