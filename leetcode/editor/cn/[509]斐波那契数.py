# 斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是： 
# 
#  
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
#  
# 
#  给你 n ，请计算 F(n) 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1
#  
# 
#  示例 2： 
# 
#  
# 输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2
#  
# 
#  示例 3： 
# 
#  
# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 30 
#  
#  Related Topics 数组 
#  👍 270 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 0: return 0
        memo = [None] * (n + 1)
        return self.helper(memo, n)

    def helper(self, memo, n):
        if n == 1 or n == 2:
            return 1
        if not memo[n]:
            memo[n] = self.helper(memo, n - 1) + self.helper(memo, n - 2)
        return memo[n]


# leetcode submit region end(Prohibit modification and deletion)

class RecursiveSolution:
    def fib(self, n: int) -> int:
        if n <= 0: return 0
        memo = [None] * (n + 1)
        return self.helper(memo, n)

    def helper(self, memo, n):
        if n == 1 or n == 2:
            return 1
        if not memo[n]:
            memo[n] = self.helper(memo, n - 1) + self.helper(memo, n - 2)
        return memo[n]


class DPSolution:
    def fib(self, n: int) -> int:
        if n <= 0: return 0
        if n == 1 or n == 2: return 1
        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 1
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]


class DPSolutionCompressed:
    def fib(self, n: int) -> int:
        if n <= 0: return 0
        if n == 1 or n == 2: return 1
        prev = 1
        curr = 1
        for i in range(3, n + 1):
            tmp = prev + curr
            prev = curr
            curr = tmp
        return curr


if __name__ == '__main__':
    sol = Solution()
    print(sol.fib(0))
