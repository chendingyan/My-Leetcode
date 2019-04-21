# -*- coding:utf-8 -*-
# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

# 思路：本题就是很直观的字符串的匹配，难点在于当遇到模式中两个特殊字符怎么处理和对于各种形式字符串的全面考虑。
# 这里采用递归的方式，每次只匹配s中一个字符（模式串pattern， 被匹配字符串s）：

# 如果 s和pattern都为空，匹配成功
# 如果pattern是空串，而s不是，匹配失败
# 如果s，pattern均不是空串(长度至少为1)，考虑到pattern中‘ * ’前字符可以出现0次，所以不能简单比较s和pattern的第一个字符是否相等，这里分为两种情况考虑：
# 如果pattern的第二个字符是‘ * ’
    # 如果s与pattern的第一个字符匹配（即s与pattern的第一个字符相等或者pattern第一个字符为‘ . ’），剩余部分有两种匹配方式：
        #(1). s后移一位，相当于认为‘ * ’前的字符在s中出现不止一次，
        #(2).pattern后移两位，相当于认为‘ * ’前的字符在s中只出现一次。
    # 否则模式串pattern后移两位，相当于认为‘ * ’前的字符在s中出现了0次；

# 如果pattern的第二个字符不是‘ * ’：如果s与pattern的第一个字符匹配（含义同上），s和pattern同时后移一位，继续匹配；否则匹配失败
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0 and len(pattern) == 0:
            return True
        if len(pattern) == 0 and len(s) > 0:
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] =='.'):
                return self.match(s[1:], pattern) or self.match(s, pattern[2:])
            else:
                return self.match(s, pattern[2:])
        else:
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s[1:], pattern[1:])
            else:
                return False
