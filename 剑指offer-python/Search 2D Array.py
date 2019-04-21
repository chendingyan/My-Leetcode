# -*- coding:utf-8 -*-
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

class Solution:
    # array 二维列表
    # 我们可以从右上角开始寻找 如果比target大 我们可以往下找 如果比target小 我们往左找
    def Find(self, target, array):
        if len(array)==0 or len(array[0]) == 0:
            return False
        i = 0
        j = len(array)-1
        while i < len(array) and j >= 0:
            if array[i][j] > target:
                j-=1
            elif array[i][j] < target:
                i+=1
            elif array[i][j] == target:
                return True
        return False



    def Find_1d(self, target, array):
        for i in array:
            if target == i:
                return True
        return False

sol = Solution()
array = [[1,2,5,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
array2 = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
ans = sol.Find(5, array)
print(ans)