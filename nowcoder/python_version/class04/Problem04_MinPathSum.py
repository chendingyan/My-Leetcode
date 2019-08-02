# 动态规划的空间压缩技巧
# 给你一个二维数组matrix，其中每个数都是正数，要求从左上角走到右下角。每 一步只能向右或者向下，沿途经过的数字要累加起来。最后请返回最小的路径和。

# 这是一个很经典的动态规划问题 但是要学会的是 空间压缩技巧 可以节省更多的空间
# 我先用原始的普通方法做一遍 然后再用动态压缩的做一遍

# 这里还有一个我错了第二遍的问题！ 二维数组的创建 在python中 二维数组的创建要用 a = [[0] * 3 for i in range(4)]

def MinPathSum1(matrix):
    dp = [[0]* len(matrix[0]) for _ in range(len(matrix))]
    dp[0][0] = int(matrix[0][0])
    for i in range(1, len(matrix[0])):
        dp[0][i] = dp[0][i-1] + matrix[0][i]
    for i in range(1, len(matrix)):
        dp[i][0] = dp[i-1][0] + matrix[i][0]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            dp[i][j] = min(dp[i-1][j]+ matrix[i][j], dp[i][j-1]+ matrix[i][j])
    print(dp)


def MinPathSum2(matrix):
    dp = [0] * len(matrix[0])
    dp[0] = matrix[0][0]
    for i in range(1, len(matrix[0])):
        dp[i] = dp[i-1]+ matrix[0][i]
    for i in range(1, len(matrix)):
        dp[0] += matrix[i][0]
        for j in range(1, len(dp)):
            dp[j] = min(dp[j] + matrix[i][j], dp[j-1] + matrix[i][j])
    print(dp)



if __name__ == '__main__':
    matrix = [
        [2,4,2,1,5,1,2,1],
        [2,2,1,4,5,2,1,3],
        [4,5,7,8,1,2,3,4],
        [5,6,7,3,1,2,4,2],
        [11,2,4,5,6,7,8,2],
        [31,23,31,22,24,52,25,19]
    ]
    print(len(matrix),len(matrix[0]))
    MinPathSum1(matrix)
    MinPathSum2(matrix)