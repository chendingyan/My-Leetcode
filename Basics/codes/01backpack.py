# 给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。
# 其中第 i 个物品的重量为 wt[i]，价值为 val[i]，现在让你用这个背包装物品，最多能装的价值是多少？

# N = 3, W = 4
# wt = [2, 1, 3]
# val = [4, 2, 3]
# 算法返回 6，选择前两件物品装进背包，总重量 3 小于 W，可以获得最大价值 6。
def backpack(N, W, wt, val):
    dp = [[0] * W for _ in range(N)]
    for i in range(1, N):
        for j in range(1, W):
            if j - wt[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
    print(dp[N - 1][W - 1])
    return dp[N - 1][W - 1]


backpack(N=3, W=4, wt=[2, 1, 3], val=[4, 2, 3])
