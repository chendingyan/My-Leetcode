# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  
#  Related Topics 数组 矩阵 模拟 
#  👍 448 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n):
        left = 0
        right = n - 1
        up = 0
        down = n - 1
        num = 1
        matrix = [[0] * n for _ in range(n)]
        while left <= right and up <= down:
            for i in range(left, right + 1):
                matrix[up][i] = num
                num += 1
            up += 1
            for i in range(up, down + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1
            for i in range(down, up - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix
# leetcode submit region end(Prohibit modification and deletion)
