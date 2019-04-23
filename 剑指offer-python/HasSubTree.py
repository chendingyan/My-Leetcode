# -*- coding:utf-8 -*-
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

# 遍历二叉树A，定位B的根节点在A中的可能位置——> 定位后，验证B是不是A当前位置的子结构。
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 == None:
            return False
        result = False
        if pRoot1.val == pRoot2.val:
            result = self.isSubtree(pRoot1, pRoot2)
        if result == False:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def isSubtree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.isSubtree(pRoot1.left, pRoot2.left) and self.isSubtree(pRoot1.right, pRoot2.right)
        return False

    def getBSTwithPreTin(self, pre, tin):
        if len(pre) == 0 | len(tin) == 0:
            return None

        root = treeNode(pre[0])
        for order, item in enumerate(tin):
            if root.val == item:
                root.left = self.getBSTwithPreTin(pre[1:order + 1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order + 1:], tin[order + 1:])
                return root

class treeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


if __name__ == '__main__':
    solution = Solution()
    preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    preorder_seq = [1, 2, 3]
    middleorder_seq = [2, 1, 3]
    treeRoot2 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    print(solution.HasSubtree(treeRoot1, treeRoot2))