# 二叉树节点间的最大距离问题
# 从二叉树的节点a出发，可以向上或者向下走，但沿途的节点只能经过一次，到达节点b时路径上的节点个数叫作a到b的距离，那么二叉树任何两个节点之间都有距离，
# 求整棵树上的最大距离。

# 树形dp套路
# 树形dp套路使用前提: 如果题目求解目标是S规则，则求解流程可以定成以每一个节点为头节点的子树在S规则下 的每一个答案，并且最终答案一定在其中

# 对于每一个节点X 1）和X无关 左树最大距离 右树最大距离 2）和X有关 左树高+1+右树高

class Node():
    def __init__(self, elem = None, left = None, right = None):
        self.elem = elem
        self.left = left
        self.right = right

class Info():
    def __init__(self, height, distance):
        self.height = height
        self.distance = distance

def process(x):
    if x is None:
        return Info(0,0)

    leftInfo = process(x.left)
    rightInfo = process(x.right)

    p1 = leftInfo.distance
    p2 = rightInfo.distance
    p3 = leftInfo.height + rightInfo.height + 1
    distance = max(p1,p2,p3)
    height = max(leftInfo.height, rightInfo.height)+1
    return Info(height, distance)


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    info = process(head)
    print(info.distance, info.height)