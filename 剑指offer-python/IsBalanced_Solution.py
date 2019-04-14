# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 思考：BST的定义为|height(lefttree)−height(righttree)|<=1|height(lefttree)−height(righttree)|<=1，原问题拆分为计算树高度和判断高度差

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        if abs(self.getHeight(pRoot.left) - self.getHeight(pRoot.right)) <= 1:
            return True
        else:
            return False

    def getHeight(self, pRoot):
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right == None:
            return 1
        leftheight = self.getHeight(pRoot.left)
        rightheight = self.getHeight(pRoot.right)
        return max(leftheight, rightheight)+1