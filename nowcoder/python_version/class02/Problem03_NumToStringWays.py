# 将给定的数转换为字符串，原则如下:1对应 a，2对应b，.....26对应z，
# 例如12258 可以转换为"abbeh", "aveh", "abyh", "lbeh" and "lyh"，个数为5，
#  编写一个函数，给出可以转换的不同字符串的个数。
def solution(n):
    arr = list(n)
    dp = [0] * (len(arr)+1)
    dp[len(arr)] = 1
    if arr[len(arr)-1] != '0':
        dp[len(arr)-1] = 1
    else:
        dp[len(arr)-1] = 0
    for i in range(len(arr)-2, -1, -1):
        if arr[i] == '0':
            dp[i] = 0
        if int(arr[i]) * 10 + int(arr[i+1]) <= 26:
            dp[i] = dp[i+1] + dp[i+2]
        else:
            dp[i] = dp[i+1]
    print(dp)
    return dp[0]

if __name__ == '__main__':
    print(solution('111143311'))
