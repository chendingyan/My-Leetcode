# -*- coding:utf-8 -*-
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
# 这道题用快排的思想 一直换 是没什么大问题的 但是 现在有一个要求 是相对位置不变 那只能用stable的sort
# 比如 insertion sort bubble sort
class Solution:
    def reOrderArray(self, array):
        # write code here
        size = len(array)
        pos = size-1
        cnt = 0
        while(cnt<size):
            if array[pos]%2==1:
                tmp = array[pos]
                for i in range(pos-1,-1,-1):
                    array[i+1] = array[i]
                array[0] = tmp
            else:
                pos -=1
            cnt +=1
        return array

sol =Solution()
array = [1]
print(sol.reOrderArray(array))