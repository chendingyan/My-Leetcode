# -*- coding:utf-8 -*-
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
# 二叉树的遍历是一个典型的递归问题，如果题目没有特殊要求，递归必然是最简单的方法，不要问为什么，记住就好了。
# 首先前序总是读取根节点，我们依照这个将中序分为左右两部分，中序里，在根节点左边的就是左子树的元素，右边的就是右子树的元素
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            leftpre = pre[1:tin.index(pre[0])+1]
            lefttin = tin[:tin.index(pre[0])]
            rightpre = pre[tin.index(pre[0])+1: len(pre)]
            righttin = tin[tin.index(pre[0])+1:len(tin)]
            root.left = self.reConstructBinaryTree(leftpre, lefttin)
            root.right = self.reConstructBinaryTree(rightpre, righttin)
            return root
