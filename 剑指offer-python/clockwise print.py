#输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
# 这道题 递归方法 试了好多次 python不太行好像
# 思路：先取矩阵的第一行，接着将剩下作为新矩阵进行一个逆时针90度的翻转，接着获取第一行，直到矩阵为空。
#
# 需要注意的点pop() 越界，翻转矩阵的时候相当于将列数据变成行数据，可以一列一列获取最后注意顺序。
# -*- coding:utf-8 -*-

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        ans = []
        while matrix :
            ans+= matrix.pop(0)
            if matrix:
                matrix = self.turnMatrix(matrix)
        return ans

    def turnMatrix(self, matrix):
        ans = []
        length = len(matrix)
        height = len(matrix[0])
        for j in range(height-1, -1,-1):
            m = []
            for i in range(length):
                m.append(matrix[i][j])
            ans.append(m)
        return ans

# matrix = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
matrix =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(len(matrix[0]))
sol = Solution()
ans = sol.turnMatrix(matrix)
print(ans)
ans =sol.printMatrix(matrix)
print(ans)