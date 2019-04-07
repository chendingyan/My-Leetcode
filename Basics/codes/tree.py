class Node():
    def __init__(self, elem = None, lchild = None, rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree():
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        node = Node(elem=elem)
        if self.root.elem == None:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treenode = self.myQueue[0]
            if not treenode.lchild:
                treenode.lchild = node
                self.myQueue.append(treenode.lchild)
            elif not treenode.rchild:
                treenode.rchild = node
                self.myQueue.append(treenode.rchild)
                print('---', self.myQueue)
                self.myQueue.pop(0)
                print(self.myQueue)
    def preorder(self, root):
        if not root:
            return False
        else:
            print(root.elem)
            self.preorder(root.lchild)
            self.preorder(root.rchild)

    def inorder(self, root):
        if not root:
            return False
        else:
            self.inorder(root.lchild)
            print(root.elem)
            self.inorder(root.rchild)

    def postorder(self,root):
        if not root:
            return False
        else:
            self.postorder(root.lchild)
            self.postorder(root.rchild)
            print(root.elem)

if __name__ == '__main__':
    """主函数"""
    elems = range(10)           #生成十个数据作为树节点
    tree = Tree()          #新建一个树对象
    for elem in elems:
        tree.add(elem)           #逐个添加树的节点

    tree.preorder(tree.root)

    # tree.inorder(tree.root)