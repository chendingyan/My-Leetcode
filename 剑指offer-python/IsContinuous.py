# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if numbers == []:
            return False
        numbers = self.delete0(numbers)
        max_num = max(numbers)
        min_num = min(numbers)
        if max_num - min_num <= 4 and self.isUnique(numbers):
            return True
        else:
            return False

    def delete0(self, numbers):
        while 0 in numbers:
            idx = numbers.index(0)
            numbers.pop(idx)

        return numbers

    def isUnique(self, numbers):
        queue = []
        for i in numbers:
            if i not in queue:
                queue.append(i)
            else:
                return False
        return True

sol = Solution()
numbers = [1,2,3,4,0]

print(sol.IsContinuous(numbers))