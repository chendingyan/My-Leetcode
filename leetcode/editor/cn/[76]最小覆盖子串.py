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
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = float('inf')
        min_seq = ""
        index = 0
        need = Counter()
        t_counter = Counter(t)
        for i in range(len(s)):
            if s[i] in t:
                need[s[i]] += 1
            while self.compare_counter(need.copy(), t_counter.copy()):
                current_length = i - index + 1
                if current_length < min_length:
                    min_seq = s[index:i+1]
                min_length = min(min_length, current_length)
                if s[index] in t:
                    need[s[index]] -= 1
                    if need[s[index]] == 0:
                        del need[s[index]]
                index += 1
        return min_seq
    def compare_counter(self, need, t_counter):
        for char in t_counter.keys():
            if need[char] < t_counter[char]:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    s = 'aa'
    t = 'aa'
    sol = Solution()
    print(sol.minWindow(s, t))
