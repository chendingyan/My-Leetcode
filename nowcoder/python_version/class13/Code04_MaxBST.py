# 求一棵树上满足BST的子树大小是的多少
# 还是和X有关 and 无关
class Node():
    def __init__(self, elem = None, left = None, right = None):
        self.elem = elem
        self.left = left
        self.right = right

class Info:
    def __init__(self, isBST, size, max_value, min_value):
        self.isBST = isBST
        self.size  = size
        self.max_value = max_value
        self.min_value = min_value

def process(x):
    if x is None:
        return Info(True, 0, -float('Inf'), float('Inf'))

    left = process(x.left)
    right = process(x.right)

    isBST = False
    size = max(left.size, right.size)
    if left.isBST and right.isBST and x.elem > left.max_value and x.elem < right.min_value:
        isBST = True
        size = left.size + right.size +1

    min_value = min(x.elem, left.min_value, right.min_value)
    max_value = max(x.elem, left.max_value, right.max_value)

    return Info(isBST, size, max_value, min_value)



if __name__ == '__main__':
    head = Node(7)
    head.left = Node(9)
    head.left.left = Node(5)
    head.left.right = Node(10)
    head.right = Node(12)
    head.right.left = Node(11)
    head.right.right = Node(13)
    head.right.right.left = Node(9)
    info = process(head)
    print(info.isBST, info.size, info.max_value, info.min_value)