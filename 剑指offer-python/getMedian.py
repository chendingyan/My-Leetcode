# -*- coding:utf-8 -*-
# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
# 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
class Solution:
    lists = []
    def Insert(self, num):
        # write code here

        self.lists.append(num)
        if len(self.lists) == 1:
            return
        j = len(self.lists)-1
        i = j
        while i>0 and num < self.lists[i-1]:
            self.lists[i] = self.lists[i-1]
            i-=1
        self.lists[i] = num

    def GetMedian(self):
        # write code here
        length = len(self.lists)
        if length %2 == 0:
            mid = length /2
            median = (self.lists[mid-1]+self.lists[mid])/2.0
        else:
            mid = length //2
            median = self.lists[mid]
        return median
sol = Solution()
sol.Insert(1)
sol.Insert(3)
sol.Insert(10)
sol.Insert(2)
sol.Insert(7)
print(sol.lists)
print(sol.GetMedian())
