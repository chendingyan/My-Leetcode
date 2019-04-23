class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self, nodelist):
        self.root = Node(nodelist[0])
        for data in nodelist[1:]:
            self.insert(data)

    def search(self, node, parent, data):
        if not node:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        elif node.data < data:
            return self.search(node.rchild, node, data)


    def insert(self, data):
        find, node, parent = self.search(self.root, self.root, data)
        if not find:
            newnode = Node(data)
            if data < parent.data:
                parent.lchild = newnode
            else:
                parent.rchild = newnode

    def delete(self, root, data):
        find, node, parent = self.search(self.root, self.root, data)
        if not find:
            return False
        else:
            # 只有一个右儿子 或者 没有儿子
            if not node.lchild:
                if parent.lchild == node:
                    parent.lchild = node.rchild
                else:
                    parent.rchild = node.rchild
                del node
            # 只有一个左儿子
            elif not node.rchild:
                if parent.lchild == node:
                    parent.lchild = node.lchild
                else:
                    parent.rchild = node.lchild
                del node
            # 有两个儿子
            else:
                pre = node.rchild
                # pre 就已经是最小的
                if not pre.lchild:
                    node.data = pre.data
                    node.rchild = pre.rchild
                    del pre
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    node.data = next.data
                    pre.lchild = next.rchild
                    del next

    # 先序遍历
    def preOrderTraverse(self, node):
        if node is not None:
            print (node.data)
            self.preOrderTraverse(node.lchild)
            self.preOrderTraverse(node.rchild)

    # 中序遍历
    def inOrderTraverse(self, node):
        if node is not None:
            self.inOrderTraverse(node.lchild)
            print(node.data)
            self.inOrderTraverse(node.rchild)

    # 后序遍历
    def postOrderTraverse(self, node):
        if node is not None:
            self.postOrderTraverse(node.lchild)
            self.postOrderTraverse(node.rchild)
            print(node.data)

    def Serialize(self, root):
        # write code here
        serial = []
        serial.append(root.data)
        if root.lchild:
            serial+=self.Serialize(root.lchild)
        else:
            serial.append('$')
        if root.rchild:
            serial+=self.Serialize(root.rchild)
        else:
            serial.append('$')
        return serial

a = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
bst = BST(a)  # 创建二叉查找树
bst.preOrderTraverse(bst.root)
# bst.delete(bst.root, 49)
# bst.inOrderTraverse(bst.root)
serial = bst.Serialize(bst.root)
print(serial)
