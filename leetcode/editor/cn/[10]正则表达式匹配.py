# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  
#  '.' 匹配任意单个字符 
#  '*' 匹配零个或多个前面的那一个元素 
#  
# 
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  
# 输入：s = "aa" p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab" p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  示例 4： 
# 
#  
# 输入：s = "aab" p = "c*a*b"
# 输出：true
# 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#  
# 
#  示例 5： 
# 
#  
# 输入：s = "mississippi" p = "mis*is*p*."
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 20 
#  0 <= p.length <= 30 
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  保证每次出现字符 * 时，前面都匹配到有效的字符 
#  
#  Related Topics 字符串 动态规划 回溯算法 
#  👍 2134 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch2(self, s, p):
        return self.dp(s, 0, p, 0)

    def dp(self, s, i, p, j):
        memo = {}
        key = str(i) + ',' + str(j)
        if key in memo.keys():
            return memo[key]
        res = False
        string_length = len(s)
        pattern_length = len(p)
        if j == pattern_length:
            return (i == string_length)
        # s= a p =ab*c*
        if i == string_length:
            if (pattern_length - j) % 2 == 1:
                return False
            else:
                for pos in range(j + 1, pattern_length, 2):
                    if p[pos] != '*':
                        return False
            return True
        # when char is equal, 2 situation
        # 1. s[i] = p[j] = alphabet, compare next
        # 2. p[j+1] = '*', jump this *, compare next next
        if s[i] == p[j] or p[j] == '.':
            if j < pattern_length - 1 and p[j + 1] == '*':
                res = self.dp(s, i, p, j + 2) or self.dp(s, i + 1, p, j)
            else:
                res = self.dp(s, i + 1, p, j + 1)
        # when char is not equal
        # s = a p = b maybe end of * like aaaab a*b, its b & *
        else:
            if j < pattern_length - 1 and p[j + 1] == '*':
                res = self.dp(s, i, p, j + 2)
            else:
                res = False
        memo[key] = res
        return res

    def isMatch(self, s, p):
        if not p: return not s
        if not s and len(p) == 1: return False
        str_length = len(s)
        pattern_length = len(p)
        dp = [[False] * (pattern_length + 1) for _ in range(str_length + 1)]
        dp[0][0] = True
        for i in range(2, pattern_length + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        for i in range(1, str_length + 1):
            str_pos = i - 1
            for j in range(1, pattern_length + 1):
                pattern_pos = j - 1
                if s[str_pos] == p[pattern_pos] or p[pattern_pos] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    if p[pattern_pos] == '*':
                        if s[str_pos] == p[pattern_pos - 1] or p[pattern_pos - 1] == '.':
                            dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                        else:
                            dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = False
        return dp[str_length][pattern_length]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = 'bb'
    p = '.bab'
    s = 'aab'
    p = 'a*b'
    s = 'aa'
    p ='a'
    sol = Solution()
    print(sol.isMatch(s, p))
