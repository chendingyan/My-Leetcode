# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0

        dp = [[0 for _ in range(len(matrix[0]))]  for _ in range(len(matrix))]
        width = len(dp[0])
        height = len(dp)
        for i in range(height):
            if matrix[i][0] == '1':
                dp[i][0] = 1

        for i in range(width):
            print(matrix[0][i])
            if matrix[0][i] == '1':
                dp[0][i] = 1


        for i in range(1,height):
            for j in range(1, width):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        print(dp)
        ans = max(map(max,dp))
        ans = ans **2
        return ans

    def sol2(self, matrix):
        if not matrix: return 0
        m,n = len(matrix[0]), len(matrix)
        dp = [int(i) for i in matrix[0]]
        print(dp)
        temp = 0
        for i in range(1, n):
            temp = dp[0]
            if matrix[i][0] == '1':
                dp[0] = 1
            for j in range(1, m):

                if matrix[i][j] == '1':
                    temp1 = dp[j]
                    dp[j] = min(temp, dp[j-1], dp[j]) + 1
                    temp = temp1
        print(dp)
if __name__ == '__main__':
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    sol = Solution()
    sol.maximalSquare(matrix)
    sol.sol2(matrix)