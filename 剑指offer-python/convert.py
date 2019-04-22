# -*- coding:utf-8 -*-
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        self.list = []
        self.inorder(pRootOfTree)
        for i in range(len(self.list)-1):
            self.list[i].right = self.list[i+1]
            self.list[i+1].left = self.list[i]
        return self.list[0]


    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.list.append(root)
        self.inorder(root.right)

