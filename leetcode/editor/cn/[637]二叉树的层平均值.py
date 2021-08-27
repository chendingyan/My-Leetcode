# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点值的范围在32位有符号整数范围内。 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 281 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        import numpy as np
        queue = []
        res = []
        queue.append(root)
        while queue:
            length = len(queue)
            layer = []
            for i in range(length):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                layer.append(cur.val)
            res.append(np.mean(layer))

        return res
# leetcode submit region end(Prohibit modification and deletion)
