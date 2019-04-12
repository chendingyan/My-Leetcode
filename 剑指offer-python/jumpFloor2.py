# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        dp = [0 for _ in range(number+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,number+1):
            sum = 0
            for j in range(1, number+1):
                sum += dp[i-j]
            dp[i] = sum
        return dp

sol = Solution()
dp = sol.jumpFloorII(4)
print(dp)
