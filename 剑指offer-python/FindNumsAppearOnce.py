# -*- coding:utf-8 -*-
# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
# 我这道题的做法 很直接 但我觉得应该考察的不是这个
# 经过寻找，我发现这道题考察的是位运算 bit manipulation
# 一个数字和自己异或一次会变成0。
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce1(self, array):
        # write code here
        if array == []:
            return []
        list1= []
        for i in array:
            if hash(i) in list1:
                print('1111')
                list1.pop(list1.index(hash(i)))
            else:
                list1.append(hash(i))
        return list1

    def FindNumsAppearOnce2(self, array):
        if len(array)<2:
            return None
        temp = array[0]
        for i in array[1:]:
            temp = temp ^ i
        if temp == 0:
            return None

        index = 0
        while temp & 1 == 0:
            temp = temp >>1
            index+=1

        num1, num2 = 0,0
        for i in array:
            if self.Bitis1(index, i):
                num1 = num1 ^ i
            else:
                num2 = num2 ^i
        return [num1, num2]

    def Bitis1(self, index, num):
        num = num >> index
        return num & 1




a = [1,2,3,1,2,4,3]
sol = Solution()
sol.FindNumsAppearOnce1(a)
