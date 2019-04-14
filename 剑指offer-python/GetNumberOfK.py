# -*- coding:utf-8 -*-
# 统计一个数字在排序数组中出现的次数。

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if data == []:
            return 0
        i = self.findKpos(data,k, 0, len(data)-1)
        if i == -1:
            ans = 0
            return ans
        start = i
        end = i
        while start> 0 and  data[start-1] == k:
            start-=1
        # print(start)
        while end < len(data)-1 and data[end+1] == k:
            end+=1
        # print(end)
        ans = end - start +1
        return ans

    def findKpos(self,data, k, start, end):
        i = (start+end)//2
        if start <= end and data[i]!=k:
            return -1
        if data[i] == k:
            return i
        while data[i]!=k:
            if data[i]<k:
                return self.findKpos(data, k, i, end)
            else:
                return self.findKpos(data,k, start,i)


data = [1,2,2,3,4,5,6,6,6]
sol =Solution()

sol.GetNumberOfK(data,9)
