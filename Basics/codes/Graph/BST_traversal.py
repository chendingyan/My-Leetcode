# Binary Search Tree's Traversal, BFS and DFS

# Example
# 输入：
###          A
#        /        \
#     B            C
#   /  \          /  \
#  D     E      F     G

# BFS输出：
# LayerOrder:
# A
# BC
# DEFG
#BFS(广度优先搜索)：
# 使用队列实现
# 每次从队列的头部取出一个元素，查看这个元素所有的下一级元素，再把它们放到队列的末尾。并把这个元素记为它下一级元素的前驱。
# 优先遍历取出元素下一级的同级元素

# DFS(深度优先搜索):
# 使用栈实现
# 每次从栈的末尾弹出一个元素，搜索所有在它下一级的元素，把这些元素压入栈中。并把这个元素记为它下一级元素的前驱。
# 优先遍历弹出元素下一级的下一级元素

class TreeNode:
    def __init__(self,x, left = None, right = None):
        self.val=x
        self.left=left
        self.right=right

    def bfs(self, root):
        result = []
        queue = []
        queue.append(root)
        while queue != []:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            result.append(node.val)
        return result

    def dfs(self, root):
        result = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            result.append(node.val)
        return result

node = TreeNode("A",TreeNode("B",TreeNode("D"),TreeNode("E")),TreeNode("C",TreeNode("F"),TreeNode("G")))
result = node.bfs(node)
print(result)
result = node.dfs(node)
print(result)


