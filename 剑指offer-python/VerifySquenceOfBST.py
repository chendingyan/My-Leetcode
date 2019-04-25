# -*- coding:utf-8 -*-
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

#首先要清楚，这道题不是让你去判断一个给定的数组是不是一个（原先）给定的二叉搜索树的对应后序遍历的结果，而是判断一个给定的数组是不是能够对应到一个具体的二叉搜索树的后序遍历结果

# 所以还是用递归的思想。

# 把数组分成三部分，比如[4,8,6,12,16,14,10]，10就是根节点，4,8,6都是左子树，12,16,14,10都是右子树，
# 然后针对左右子树再去判断是不是符合根节点、左右子树这一个规律（左子树都比根节点小，右子树都比根节点大）
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        pass