# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
#  Related Topics 数组 矩阵 模拟 
#  👍 823 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix):
        res = []
        left, right, up, down = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        shape = (right+1) * (down+1)
        while left <= right and up <= down:
            for i in range(left, right + 1):
                res.append(matrix[up][i])
            up += 1
            for i in range(up, down + 1):
                res.append(matrix[i][right])
            right -= 1
            for i in range(right, left - 1, -1):
                res.append(matrix[down][i])
            down -= 1
            for i in range(down, up - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res[:shape]
# leetcode submit region end(Prohibit modification and deletion)
