# 给定一个二叉树，返回它的 后序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [3,2,1] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 深度优先搜索 二叉树 
#  👍 656 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        stack = []
        res = []
        if not root:
            return res
        stack.append(root)
        while len(stack)!=0:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        res.reverse()
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        return self.traversal([], root)

    def traversal(self, arr, root):
        if not root:
            return arr
        self.traversal(arr, root.left)
        self.traversal(arr, root.right)
        arr.append(root.val)
        return arr
# leetcode submit region end(Prohibit modification and deletion)
