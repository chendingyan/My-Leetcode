# -*- coding:utf-8 -*-
# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
# 第一步：两个数按位取亦或。获得的值为不考虑进位时的和。
# 第二步：两个数按位取与。获得的值为（当两个数某一位同为1时）两个数求和时需要进位的位置。每次讲该数（在代码中表示为num2）左移一位，表示进位后。
# 循环第一二步，直至两数的和没有进位位为止。
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2:
            mainpart = num1^num2
            num2 = (num1&num2)<<1
            num1 = mainpart
        return num1



num1 = 3 # 0011
num2 = 5 # 0101
#          1000
# 0011+0101 =
print(num1 ^ num2) # 0110 = 6
print(num1 & num2) # 0001 = 1
# 0110 ^ 0010 = 1001

xor = num1 ^ num2
print(xor == 0)

sol = Solution()
print(sol.Add(2,14))