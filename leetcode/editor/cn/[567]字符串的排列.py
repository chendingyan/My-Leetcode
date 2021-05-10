# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。 
# 
#  换句话说，第一个字符串的排列之一是第二个字符串的 子串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#  
# 
#  示例 2： 
# 
#  
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#  
# 
#  
# 
#  提示： 
# 
#  
#  输入的字符串只包含小写字母 
#  两个字符串的长度都在 [1, 10,000] 之间 
#  
#  Related Topics 双指针 Sliding Window 
#  👍 347 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left, right = 0, len(s1) - 1
        need = dict.fromkeys(s1, 0)
        window = {}
        for str in s1:
            need[str] += 1
        for i in range(left, right):
            window[s2[i]] = window.setdefault(s2[i], 0) + 1
        while right < len(s2):
            window[s2[right]] = window.setdefault(s2[right], 0) + 1
            if need == window:
                return True
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                window.pop(s2[left])
            left += 1
            right += 1
        return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    s1 = 'horse'
    s2 = 'ros'
    sol = Solution()
    print(sol.checkInclusion(s1, s2))
