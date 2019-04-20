# -*- coding:utf-8 -*-
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007

# 拷贝该数组后对拷贝的数组排序。计算数组中的最小值在原始数组中出现的位置，统计原始数组中最小值前面的个数，之后在原始数组中去掉最小值。重复上述步骤。

# Mergesort 改版那种做法我有点做不来
class Solution:
    def InversePairs(self, data):
        # write code here
        count = 0
        sort = sorted(data)
        while len(sort)>1:
            min = sort.pop(0)
            index = data.index(min)
            data.pop(index)
            count+=index
        return count

    def InversePairs2(self, data):
        if not data:
            return 0
        dataCopy = data.copy()
        return self.InverseRecur(data, dataCopy, 0, len(data)-1)

    def InverseRecur(self, data, dataCopy, start, end):
        if start == end:
            return 0
        mid = (start+end)//2
        left = self.InverseRecur(data, dataCopy, start, mid)
        right = self.InverseRecur(data, dataCopy, mid, end)


sol = Solution()
data = [1,2,3,4,5,6,7,0]
print(sol.InversePairs(data))
