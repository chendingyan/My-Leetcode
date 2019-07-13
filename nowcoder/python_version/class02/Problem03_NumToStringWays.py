# 将给定的数转换为字符串，原则如下:1对应 a，2对应b，.....26对应z，
# 例如12258 可以转换为"abbeh", "aveh", "abyh", "lbeh" and "lyh"，个数为5，
#  编写一个函数，给出可以转换的不同字符串的个数。
def NumToStringWays(str):
    dp = [0]*(len(str)+1)
    dp[len(str)-1] = 0
    if str[len(str)-1] != '0':
        dp[len(str)-2] = 1
    if int(str[len(str)-2])*10 + int(str[len(str)-1]) < 27:
        dp[len(str)-3] = 2
    else:
        dp[len(str)-3] = 1

    for i in range(len(str)-3, -1, -1):
        num = int(str[i-1])*10+int(str[i])
        if num<27:
            dp[i] = dp[i+1] + dp[i+2]
        else:
            dp[i] = dp[i+1]
    print(dp)
    return dp[0]

if __name__ == '__main__':
    print(NumToStringWays('111143311'))
