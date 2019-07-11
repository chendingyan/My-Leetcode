# 小虎去附近的商店买苹果，奸诈的商贩使用了捆绑交易，只提供6个每袋和8个 每袋的包装包装不可拆分。
# 可是小虎现在只想购买恰好n个苹果，小虎想购买尽 量少的袋数方便携带。如果不能购买恰好n个苹果，小虎将不会购买。
# 输入一个 整数n，表示小虎想购买的个苹果，返回最小使用多少袋子。如果无论如何都不 能正好装下，返回-1。

# 动态规划 转打表
def AppleMinBags(n):
    if n < 6 or n == 7:
        return -1
    if n == 6 or n == 8:
        return 1
    dp = [1000000]* (n+1)
    dp[6] = 1
    dp[8] = 1
    for i in range(9, n+1):
        dp[i] = min(dp[i-6]+1, dp[i-8]+1)
    if dp[n] > 50000:
        return -1
    else:
        return dp[n]

def AppleMinBags_Awesome(n):
    if n < 18:
        if n == 6 or n == 8:
            return 1
        elif n == 12 or n == 14 or n == 16:
            return 2
        else:
            return -1
    else:
        if n % 2 == 1:
            return -1
        else:
            return int((n-18)/8) + 3

if __name__ == '__main__':
    for i in range(0,100):
        print(i , AppleMinBags_Awesome(i) == AppleMinBags(i))
