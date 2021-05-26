# Imagine you have a special keyboard with the following keys:
#
# Key 1: (A): Print one 'A' on screen.
#
# Key 2: (Ctrl-A): Select the whole screen.
#
# Key 3: (Ctrl-C): Copy selection to buffer.
#
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
#
# Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.
#
# Example 1:
#
# Input: N = 3
# Output: 3
# Explanation:
# We can at most get 3 A's on screen by pressing following key sequence:
# A, A, A
# Example 2:
#
# Input: N = 7
# Output: 9
# Explanation:
# We can at most get 9 A's on screen by pressing following key sequence:
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

class Solution:
    def maxA(self, N):
        return self.dp(N, 0, 0)

    def dp(self, remain_N, current_A, copy_A):
        if remain_N <= 0:
            return current_A
        return max(
            self.dp(remain_N - 1, current_A + 1, copy_A),
            self.dp(remain_N - 2, current_A, current_A),
            self.dp(remain_N - 1, current_A + copy_A, copy_A)
        )

    def maxA2(self, N):
        dp = [0] * N
        dp[0] = 1
        for i in range(1, N):
            dp[i] = dp[i - 1] + 1
            for j in range(3, i + 1):
                max_value = dp[j - 3] * (i - j + 2)
                dp[i] = max(dp[i], max_value)
        return dp[N - 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxA(13))
    print(sol.maxA(7))
    print(sol.maxA2(13))
    print(sol.maxA2(7))
