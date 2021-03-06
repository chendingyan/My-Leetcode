# -*- coding:utf-8 -*-
# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        count = 0
        for i in range(0, rows):
            for j in range(0, cols):
                if self.isValid(threshold, i, j):
                    count+=1
        return count


    def isValid(self, k, x, y):
        x = str(x)
        y = str(y)
        sum = 0
        for i in range(0, len(x)):
            sum+= int(x[i])
        for i in range(0, len(y)):
            sum+= int(y[i])

        if sum <= k:
            return True
        else:
            return False

sol = Solution()
# sol.isValid(0, 35,37)
print(sol.movingCount(18,30,30))