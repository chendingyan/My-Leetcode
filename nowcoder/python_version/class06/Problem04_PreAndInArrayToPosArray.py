# 已知一棵二叉树中没有重复节点，并且给定了这棵树的中序遍历数组和先序遍历 数组，返回后序遍历数组。
# 比如给定:
# int[] pre = { 1, 2, 4, 5, 3, 6, 7 };
# int[] in = { 4, 2, 5, 1, 6, 3, 7 }; 返回:
# {4,5,2,6,7,3,1}
# 这是一个递归问题  pre中 1 在第一个 说明 1 是root 那么在in里找到1 1的左边 4 2 5 是左树 右边 6 3 7是右树 所以 pre的后面 2 4 5 是左树 3 6 7 是右树
# 然后2 4 5 里面 2 在第一个 在in中 2 的左树 是 4  右树 是5  从而找到递归策略

def PreAndInToPos(pre, inorder, pos):
    if not pre or not inorder:
        return
    if len(pre) == 1 and len(inorder) == 1:
        pos.append(pre[0])
        return pre[0]
    root = pre[0]
    index = inorder.index(root)
    left_inorder = inorder[0:index]

    right_inorder = inorder[index+1:]
    left_pre = pre[1:index+1]
    right_pre = pre[index+1:]
    PreAndInToPos(left_pre, left_inorder,pos)
    PreAndInToPos(right_pre, right_inorder,pos)
    pos.append(root)
    return pos
if __name__ == '__main__':
    pre = [1,2,4,5,3,6]
    inorder = [4,2,5,1,6,3]
    # pre = [2,4,5]
    # inorder = [4,2,5]
    pos = []
    pos = PreAndInToPos(pre, inorder, pos)
    print(pos)