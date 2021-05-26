# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。 
# 
#  
# 
#  示例 1: 
# 输入: 
# 
#  "bbbab"
#  
# 
#  输出: 
# 
#  4
#  
# 
#  一个可能的最长回文子序列为 "bbbb"。 
# 
#  示例 2: 
# 输入: 
# 
#  "cbbd"
#  
# 
#  输出: 
# 
#  2
#  
# 
#  一个可能的最长回文子序列为 "bb"。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 只包含小写英文字母 
#  
#  Related Topics 动态规划 
#  👍 450 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        print(dp)
        return dp[0][n - 1]

    def longestPalindromeSubseq2(self, s):
        n = len(s)
        pre = [0] * n
        cur = [0] * n
        for i in range(n - 2, -1, -1):
            pre[i+1] = 1
            cur[i] = 1
            for j in range(i + 1, n):

                if s[i] == s[j]:
                    cur[j] = pre[j - 1] + 2
                else:
                    cur[j] = max(cur[j - 1], pre[j])
            pre = cur.copy()
        return cur[-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = 'bbbab'
    sol = Solution()
    print(sol.longestPalindromeSubseq(s))
    print(sol.longestPalindromeSubseq2(s))
