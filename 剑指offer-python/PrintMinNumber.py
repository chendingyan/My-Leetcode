# -*- coding:utf-8 -*-
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
# 先将整数数组转为字符串数组，然后用比较器实现字符串比较大小。如果有字符串A和B， A + B < B + A，则A在前；反之B在前。最后将字符串数组连接去除返回值左侧的0。

# (1)我们可以先思考只有两个数字的情况： [3,32] ，可以看出来 332>323 因此需要把数组改变为 [32,3] ；
#（2)对于有三个数字的情况： [3,32,321] 我们两两进行比较， 332>323 于是，将 3 与 32 交换位置变成 [32,3,321] 而 3321>3213 于是将 3 与 321 继续交换位置到 [32,321,3] ；接着我们继续使用 32 进行比较，由于 32321>32132 将 32与321 进行位置交换为 [321,32,3] 此时，将数组链接起来变成 321323 即为最小的数。
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        list1 = self.quicksort(numbers)
        ans = ''.join(list1)
        return ans

    def quicksort(self,numbers):
        numbers = list(map(str, numbers))
        if len(numbers)<2:
            return numbers[:]
        left = self.quicksort(i for i in numbers[1:] if (i+numbers[0]) < (numbers[0]+i))
        right = self.quicksort(i for i in numbers[1:] if (i+numbers[0]) >= (numbers[0]+i))
        return left+list(numbers[0])+right

    def PrintMinNumber2(self, numbers):
        numbers = list(map(str, numbers))
        numbers.sort(cmp = lambda x,y: cmp(x+y,y+x))
        ans = ''.join(numbers)
        return ans

number = [3,32,321,123]
sol = Solution()
# print(sol.quicksort(number))
print(sol.PrintMinNumber(number))
print(sol.PrintMinNumber2(number))
