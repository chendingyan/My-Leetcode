# 翻转一棵二叉树。 
# 
#  示例： 
# 
#  输入： 
# 
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9 
# 
#  输出： 
# 
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1 
# 
#  备注: 
# 这个问题是受到 Max Howell 的 原问题 启发的 ： 
# 
#  谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 975 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = []
        queue.append(root)
        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.pop(0)
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

    def recursive_solution(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.recursive_solution(root.left)
        self.recursive_solution(root.right)
        return root

    def dfs_solution(self, root):
        if not root:
            return None
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return root

    def bfs_solution(self, root):
        if not root:
            return None
        queue = []
        queue.append(root)
        while queue:
            length = len(queue)
            for i in range(length):
                cur = queue.pop(0)
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

# leetcode submit region end(Prohibit modification and deletion)
