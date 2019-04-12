# 大家都知道斐波那契数列 f(n) = f(n-1) + f(n-2)，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        queue = [0,1]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(2, n+1):
                queue.append(queue[i-1]+queue[i-2])
            return queue.pop()