# -*- coding:UTF-8 -*-
# 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
# 尝试一下双指针？

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        list = range(1, tsum+1)
        p1 = 1
        p2 = 2
        ans = []
        while True:
            mysum = sum(range(p1,p2+1))
            if mysum > tsum:
                p1+=1
            elif mysum < tsum:
                p2+=1
            elif mysum == tsum:
                slist = range(p1,p2+1)
                print(slist)
                ans.append(slist)
                p1+=1
            if p2 > (tsum+1)/2:
                return ans

sol = Solution()
ans = sol.FindContinuousSequence(9)
print(ans)
