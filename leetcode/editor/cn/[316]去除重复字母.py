# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。 
# 
#  注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct
# -characters 相同 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "bcabc"
# 输出："abc"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbacdcbc"
# 输出："acdb" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 由小写英文字母组成 
#  
#  Related Topics 栈 贪心算法 字符串 
#  👍 531 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        is_exist = {}
        for char in s:
            is_exist[char] = False
        for char in s:
            count[char] -= 1
            if not is_exist[char]:
                while len(stack) > 0 and stack[-1] > char:
                    if count[stack[-1]] == 0:
                        break
                    else:
                        is_exist[stack.pop()] = False
                stack.append(char)
                is_exist[char] = True
        return ''.join(stack)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = 'bcabc'
    s = "cbacdcbc"
    sol = Solution()
    print(sol.removeDuplicateLetters(s))
