# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 02:26:37 2021

@author: dla05
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None: return
        l=[]
        if root.left!=None : 
            l=l+self.inorderTraversal(root.left)
        l.append(root.val)
        if root.right!=None : 
            l=l+self.inorderTraversal(root.right)
        return l