# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return []
        serial = []
        serial.append(root.val)
        if root.left:
            serial+=self.Serialize(root.left)
        else:
            serial.append('$')
        if root.right:
            serial+=self.Serialize(root.right)
        else:
            serial.append('$')
        return serial


    def Deserialize(self, s):
        # write code here
        if s != []:
            val = s.pop(0)
            if val != '$':
                pRoot = TreeNode(val)
            else:
                return None
            pRoot.left = self.Deserialize(s)
            pRoot.right = self.Deserialize(s)
            return pRoot
        else:
            return None