# -*- coding:utf-8 -*-
# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        heapq.heapify(tinput)
        res=[]
        for i in range(0,k):
            res.append(heapq.heappop(tinput))

        return res
sol = Solution()
data= [4,5,1,6,2,7,3,8]
res = sol.GetLeastNumbers_Solution(data, 4)
print(res)