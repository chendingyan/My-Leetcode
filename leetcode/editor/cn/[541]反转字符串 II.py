# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。 
# 
#  
#  如果剩余字符少于 k 个，则将剩余字符全部反转。 
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abcd", k = 2
# 输出："bacd"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 仅由小写英文组成 
#  1 <= k <= 104 
#  
#  Related Topics 双指针 字符串 
#  👍 134 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseStr(self, s, k):
        from functools import reduce
        s = list(s)
        for i in range(0, len(s), 2 * k):
            if i + k < len(s):
                right = i + k
            else:
                right = len(s)
            pre_k = s[i:right]
            s[i:right] = list(reversed(pre_k))
        return reduce(lambda x, y: x + y, s)


# leetcode submit region end(Prohibit modification and deletion)
def sub_space(s):
    s = list(s)
    count = 0
    for i in s:
        if i == ' ':
            count += 1
    res = [None] * (len(s) + 2 * count)
    right = len(res) - 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            res[right - 2:right+1] = '%20'
            right -= 3
        else:
            res[right] = s[i]
            right -= 1
    return ''.join(res)


if __name__ == '__main__':
    # sol = Solution()
    # s = 'abcdefg'
    # k = 2
    # print(sol.reverseStr(s, k))
    s = "We are happy."
    print(sub_space(s))
