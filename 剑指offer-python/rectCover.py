# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

# 仍然是斐波那契数列 原因是 https://blog.csdn.net/fuxuemingzhu/article/details/79502151
# 不用找规律 用这个角度去想问题 很快就能解决

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        queue = [1, 1]
        if number == 0:
            return 0
        elif number == 1:
            return 1
        else:
            for i in range(2, number + 1):
                queue.append(queue[i - 1] + queue[i - 2])
        return queue.pop()
