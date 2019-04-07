# https://blog.csdn.net/shulixu/article/details/86376621
# 机智的DP解法
# 含有n个结点的二叉搜索树，其根节点可为1~n中的任一结点。当根节点为k时，其左子树共有k-1个结点，右子树共有n-k个结点。
# 令f(n) 为n个结点时的二叉搜索树的数目。令num(k)为顶点为k时BST的数目。所以num(k)=f(k-1)*f(n-k);计算f(n)则求num(1)~num(n)之和.
# G[n]代表n个node的BST数目
# F[i,n]代表root为i时， n个node的BST数目
# F[i,n] = G[i-1]*G[n-i], 1 <= i <= n
# G[n] = F[1,n]+F[2,n]+....+F[n,n]
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0] * (n + 1)
        count[0] = 1

        for i in range(1, n + 1):
            for j in range(0, i):
                count[i] += count[j] * count[i - j - 1]
        print(count)
        return count[n]

if __name__ == '__main__':
    sol = Solution()
    sol.numTrees(3)