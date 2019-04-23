# -*- coding:utf-8 -*-
import sys
# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
class Solution:
    def __init__(self):
        self.items = []
    def push(self, node):
        # write code here
        self.items.append(node)
    def pop(self):
        # write code here
        return self.items.pop()
    def top(self):
        # write code here

        return self.items[-1]
    def min(self):
        # write code here
        return min(self.items)


sol = Solution()
sol.push(3)
print(sol.min())
sol.push(4)
sol.push(2)
sol.push(3)
print(sol.min())
print(sol.pop())
print(sol.min())
print(sol.pop())
print(sol.min())
print(sol.pop())
print(sol.min())
sol.push(0)
print(sol.min())