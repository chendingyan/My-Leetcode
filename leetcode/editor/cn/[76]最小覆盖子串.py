# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 105 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 1143 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # [left, right]
        left = 0
        right = 0
        window = {}
        need = {}
        valid = 0
        start = 0
        min_len = len(s) + 1
        window = dict.fromkeys(t, 0)
        need = dict.fromkeys(t, 0)
        for char in t:
            need[char] += 1
        while right != len(s):
            if s[right] in window.keys():
                window[s[right]] += 1
                if window[s[right]] == need[s[right]]:
                    valid += 1

            right += 1

            while valid == len(need):
                if right - left < min_len:
                    start = left
                    min_len = right - left

                if s[left] in window.keys():
                    window[s[left]] -= 1
                    if window[s[left]] < need[s[left]]:
                        valid -= 1
                left += 1
        if min_len == len(s) + 1:
            return ""
        return s[start:start + min_len]


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    s = 'a'
    t = 'a'
    sol = Solution()
    print(sol.minWindow(s, t))
