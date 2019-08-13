# 给定两个字符串str1和str2，再给定三个整数ic、dc和rc，分别代表插入、删除和替换一个字符的代价，返回将str1编辑成str2的最小代价。
# 【举例】
# str1="abc"，str2="adc"，ic=5，dc=3，rc=2 从"abc"编辑成"adc"，把'b'替换成'd'是代价最小的，所以返回2
# str1="abc"，str2="adc"，ic=5，dc=3，rc=100 从"abc"编辑成"adc"，先删除'b'，然后插入'd'是代价最小的，所以返回8
# str1="abc"，str2="abc"，ic=5，dc=3，rc=2 不用编辑了，本来就是一样的字符串，所以返回0

# 无敌经典题 经典动态规划
# dp[i][j] -> str1[0...i] 编辑到 str[0...j]的代价


def EditCost(str1, str2, ic,dc,rc):
    height = len(str1)+1
    width = len(str2)+1
    dp = [[0 for _ in range(width)] for _ in range(height) ]


    for i in range(height):
        dp[i][0] = i * dc

    for j in range(width):
        dp[0][j] = j * ic

    for i in range(1, height):
        for j in range(1, width):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + rc

            dp[i][j] = min(dp[i-1][j] + dc , dp[i][j])
            dp[i][j] = min(dp[i][j-1] + ic, dp[i][j])
    print(dp[height-1][width-1])

if __name__ == '__main__':
    str1 = 'abc'
    str2 = 'adc'
    ic = 5
    dc = 3
    rc = 2
    EditCost(str1, str2, ic ,dc, rc)





