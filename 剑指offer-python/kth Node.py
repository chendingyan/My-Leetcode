# -*- coding:utf-8 -*-
# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
# 这道题的重点！是二叉搜索树！ 是BST 大小排序过的 那其实只要inorder排序就够了
# 但是要返回对应节点的TreeNode 所以是要变相更改一下inorder
# 中序遍历一共三步：
# 1. 递归左子树
# 2. 存储根节点的值
# 3. 递归右子树
#
# 本题也需要三步：
# 1. 递归左子树，并判断有无返回节点。如果有，停止递归，返回所要返回的节点。
# 2. 当左子树没有返回节点时，判断当前的根节点是不是第k个遍历到的值（即第k大）。如果是，则返回该节点，停止递归。
# 3. 当左子树和根节点都没有返回节点时，递归右子树，并判断有无返回节点。如果有，停止递归，返回所要返回的节点。

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    count = 0
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return None

        node = self.KthNode(pRoot.left, k)
        if node:
            return node
        self.count+=1
        if self.count == k:
            return pRoot

        node = self.KthNode(pRoot.right,k)
        if node:
            return node