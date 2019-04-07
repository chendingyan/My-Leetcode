# https://blog.csdn.net/shulixu/article/details/86376621
# 机智的DP解法
# 含有n个结点的二叉搜索树，其根节点可为1~n中的任一结点。当根节点为k时，其左子树共有k-1个结点，右子树共有n-k个结点。
# 令f(n) 为n个结点时的二叉搜索树的数目。令num(k)为顶点为k时BST的数目。所以num(k)=f(k-1)*f(n-k);计算f(n)则求num(1)~num(n)之和.
# G[i]代表i个node的BST数目
# G[i] = F[1,i]+F[2,i]+....+F[i,i]
# F[j,i]代表root为j时， i个node的BST数目
# F[j,i] = G[j-1]*G[i-j], 1 <= j <= i

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0] * (n + 1)
        count[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i+1):
                count[i] += count[j-1] * count[i - j]
        print(count)
        return count[n]

if __name__ == '__main__':
    sol = Solution()
    sol.numTrees(3)