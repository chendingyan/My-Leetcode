# -*- coding:utf-8 -*-
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        save = dict()
        queue = []
        for i in numbers:
            if i not in save:
                save[i] = 1
                queue.append(i)
            else:
                save[i]+=1
            if save[i] > len(numbers)//2:
                return i
        return 0


sol = Solution()
numbers = [2,2,2,2,2,1,3,4,5]
ans = sol.MoreThanHalfNum_Solution(numbers)
print(ans)
print(1//2)
