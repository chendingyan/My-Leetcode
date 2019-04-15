# -*- coding:utf-8 -*-
# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
# 这道题 看了之后想用递归做 但其实可以外开空间 queue， 用list去储存，这样就不用递归了
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue = [pRoot]
        result = []
        while queue:
            row =[]
            for i in queue:
                row.append(i.val)
            result.append(row)
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return result