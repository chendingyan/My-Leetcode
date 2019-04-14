# -*- coding:utf-8 -*-
# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right == None:
            return 1
        ld = self.TreeDepth(pRoot.left)
        rd = self.TreeDepth(pRoot.right)
        return max(ld, rd)+1