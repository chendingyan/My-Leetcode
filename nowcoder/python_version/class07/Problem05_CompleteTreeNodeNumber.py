# 求完全二叉树节点的个数 小于O(n)复杂度

# 字节跳动新题 完全二叉树 最后一个节点 返回
# 假设 这棵树的depth = n (作为一个完全二叉树 可以一直left求)
# 找右树的最左的节点 如果这个节点depth=n 说明左树 是完全的 然后再递归找这个右树 的node number
# 如果这个右树最左节点的depth = n-1 说明右树是一个完全的 可以计算这个右树 再递归找左树

# 用递归和迭代两种方式 都可以解决

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def getLevel(root):
    level = 0
    while root:
        root = root.left
        level+=1
    return level


def NodeNumber(root):

    node = 0
    level = getLevel(root)
    while root:
        if getLevel(root.right) == level-1:
            #左树 是完全的
            node += 2 ** (level-1)
            root = root.right
        else:
            node += 2 ** (level-2)
            root = root.left
        level-=1
    return node

def NodeNumber2(root):

    level = getLevel(root)
    if getLevel(root) == 1:
        return 1
    if getLevel(root.right) == level-1:
        return 2**(level-1) + NodeNumber(root.right)
    else:
        return 2**(level-2) + NodeNumber(root.left)

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    head.left.left.left = Node(8)
    head.left.left.right = Node(9)
    print(getLevel(head))
    print(NodeNumber(head))
    print(NodeNumber2(head))