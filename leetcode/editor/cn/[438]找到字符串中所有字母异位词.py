# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。 
# 
#  字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。 
# 
#  说明： 
# 
#  
#  字母异位词指字母相同，但排列不同的字符串。 
#  不考虑答案输出的顺序。 
#  
# 
#  示例 1: 
# 
#  
# 输入:
# s: "cbaebabacd" p: "abc"
# 
# 输出:
# [0, 6]
# 
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入:
# s: "abab" p: "ab"
# 
# 输出:
# [0, 1, 2]
# 
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
#  
#  Related Topics 哈希表 
#  👍 524 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        left = 0
        right = len(p) - 1
        need = Counter(p)
        window = Counter(s[left:right])
        res = []
        while right < len(s):
            window[s[right]] += 1
            if window == need:
                res.append(left)
            window[s[left]] -= 1
            if window[s[left]] == 0:
                window.pop(s[left])
            right += 1
            left += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = "cbaebabacd"
    p = 'abc'
    sol = Solution()
    print(sol.findAnagrams(s, p))
