# 二叉树每个结点都有一个int型权值，给定一棵二叉树，要求计算出从根结点到 叶结点的所有路径中，权值和最大的值为多少。
def TreeDepth(pRoot):
    # write code here
    if pRoot == None:
        return 0
    if pRoot.left == None and pRoot.right == None:
        return pRoot.weight
    ld = TreeDepth(pRoot.left)
    rd = TreeDepth(pRoot.right)
    return max(ld, rd) + pRoot.weight