# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 02:29:19 2021

@author: dla05
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None: return
        l=[]
        if root.left!=None : 
            l=l+self.postorderTraversal(root.left)
        if root.right!=None : 
            l=l+self.postorderTraversal(root.right)
        l.append(root.val)
        return l