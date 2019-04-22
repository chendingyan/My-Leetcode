# -*- coding:utf-8 -*-
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
class Solution:
    # 说实话 这一种方法  我也不知道为什么
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = n&(n-1)
            count+=1
        return count
    #这一种方法很好理解 就是把每个数的最低位和1 and 如果最低位是1  就是1 如果最低位是0  就是0 那么再一直右移n就对了
    def NumberOf1_(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += n &1
            n = n >>1
        return count

sol = Solution()
print(sol.NumberOf1(-1))
print(sol.NumberOf1_(-1))
