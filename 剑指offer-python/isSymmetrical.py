# -*- coding:utf-8 -*-
# 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return self.Symmetrical(pRoot.left, pRoot.right)

    def Symmetrical(self, leftNode, rightNode):
        if leftNode == None and rightNode == None:
            return True
        if leftNode and rightNode:
            # 这个地方原来写的时候 出了大问题
            # "镜像" 所比较的东西 不是左边对称和右边对称 是左右加起来对称 比较的东西出错了
            # return leftNode.val == rightNode.val and self.Symmetrical(leftNode.left, leftNode.right) and self.Symmetrical(rightNode.left, rightNode.right)
            return leftNode.val == rightNode.val and self.Symmetrical(leftNode.left,
                                                                      rightNode.right) and self.Symmetrical(
                leftNode.right, rightNode.left)
        else:
            return False


