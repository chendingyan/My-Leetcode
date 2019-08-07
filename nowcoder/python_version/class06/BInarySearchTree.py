# 在这里复习一下二叉搜索树的知识 注意 二叉搜索树 和二叉树 的不同

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self, nodelist):
        if nodelist is None:
            return
        self.root = Node(nodelist[0])
        if len(nodelist) > 1:
            for data in nodelist[1:]:
                self.insert(data)

    def search(self, node, parent, data):
        if not node:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.left, node, data)
        elif node.data < data:
            return self.search(node.right, node, data)

    def insert(self, data):
        find, node, parent = self.search(self.root, self.root, data)
        if not find:
            newnode = Node(data)
            if data < parent.data:
                parent.left = newnode
            else:
                parent.right = newnode

    def delete(self, data):
        find, node, parent = self.search(self.root, self.root, data)
        if not find:
            return False
        else:
            # 只有一个右儿子 或者 没有儿子
            if not node.left:
                if parent.left == node:
                    parent.left = node.right
                else:
                    parent.right = node.right
                del node

            # 只有一个左儿子
            elif not node.right:
                if parent.left == node:
                    parent.left = node.left
                else:
                    parent.right = node.left
                del node
            # 有两个儿子 要找到他右边最小的 就是比他大的node里面最小的
            else:

                pre = node.right
                # pre已经是最小的了
                if not pre.left:
                    node.data = pre.data
                    node.right = pre.right
                    del pre
                else:
                    next = pre.left
                    while next.left is not None:
                        pre = next
                        next = pre.left
                    node.data = next.data
                    pre.left = next.right
                    del next
