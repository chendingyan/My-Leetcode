# -*- coding:utf-8 -*-
# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
# 思路：中序遍历的顺序为LVR
# 则有以下三种情况：
# a. 如果该结点存在右子结点，那么该结点的下一个结点是右子结点树上最左子结点
# b. 如果该结点不存在右子结点，且它是它父结点的左子结点，那么该结点的下一个结点是它的父结点
# c. 如果该结点既不存在右子结点，且也不是它父结点的左子结点，则需要一路向祖先结点搜索，直到找到一个结点，该结点是其父亲结点的左子结点。
# 如果这样的结点存在，那么该结点的父亲结点就是我们要找的下一个结点
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            rightnode = pNode.right
            while rightnode.left:
                rightnode = rightnode.left
            return rightnode
        else:
            # 这一段考虑情况十分的复杂 但可以极其简单的化简成下面几句话
            # if pNode.next == None:
            #     return None
            # if pNode.next.left == pNode:
            #     return pNode.next
            # elif pNode.next.right == pNode:
            #     parent = pNode.next
            #     while parent.next!= None and parent.next.right == parent:
            #         parent = parent.next
            #     if parent.next!= None and parent.next.left == parent:
            #         return parent.next
            #     elif parent.next == None:
            #         return None
            parent = pNode.next
            while parent and parent.right == pNode:
                pNode = parent
                parent = parent.next
            return parent


