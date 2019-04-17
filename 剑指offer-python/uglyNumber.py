# -*- coding:utf-8 -*-
# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。
# 求按从小到大的顺序的第N个丑数。
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0
            return 0
        i = 1
        ugly = [1]
        i2,i3,i5 = 0,0,0
        while len(ugly) <= index:
            min_num = min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
            ugly.append(min_num)

            if ugly[i] == ugly[i2]*2:
                i2+=1
            if ugly[i] == ugly[i3]*3:
                i3+=1
            if ugly[i] == ugly[i5]*5:
                i5+=1
            i+=1
        return ugly[index-1]

sol = Solution()
print(sol.GetUglyNumber_Solution(1))
