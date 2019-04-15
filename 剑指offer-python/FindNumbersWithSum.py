# -*- coding:utf-8 -*-
#输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
# hash
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        p1 = 0
        p2 = len(array)-1
        list1 = []
        while p2>p1:
            if array[p1]+array[p2] > tsum:
                p2-=1
            elif array[p1]+array[p2] < tsum:
                p1+=1
            else:
                num1 = array[p1]
                num2 = array[p2]
                list1.append((num1,num2))
                return list1


sol = Solution()
array = [1,2,3,4,5,6,7,8,9,10]
tsum = 12
list1 = sol.FindNumbersWithSum(array, tsum)
print(list1)