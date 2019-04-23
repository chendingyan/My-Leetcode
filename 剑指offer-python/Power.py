# -*- coding:utf-8 -*-
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent < 0:
            base = 1/base
            exponent = - exponent
        return self.helper(base, exponent)
    def helper(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        return base * self.Power(base, exponent-1)

sol = Solution()
base = 2.0
exponent = -1
print(sol.Power(base, exponent))