# -*- coding:utf-8 -*-
# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        height = 1
        if not pRoot:
            return []
        ans = []
        queue = [pRoot]
        while queue:
            row = []
            for i in queue:
                row.append(i.val)
            if height % 2 == 0:
                row.reverse()
            ans.append(row)

            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            height+=1
        return ans