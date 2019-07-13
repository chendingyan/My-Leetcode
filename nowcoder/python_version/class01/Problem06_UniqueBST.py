# 给定一个非负整数n，代表二叉树的节点个数。返回能形成多少种不同的二叉树结构
#动态规划！

def UniqueBST(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        for left in range(0,i):
            dp[i] += dp[left] * dp[i-1-left]
    return dp[n]

if __name__ == '__main__':
    for i in range(0,13):
        print(UniqueBST(i))