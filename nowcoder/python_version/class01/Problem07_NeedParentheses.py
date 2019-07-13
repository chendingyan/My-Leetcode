# 一个完整的括号字符串定义规则如下:
# 1空字符串是完整的。
# 2如果s是完整的字符串，那么(s)也是完整的。
# 3如果s和t是完整的字符串，将它们连接起来形成的st也是完整的。
# 例如，"(()())", ""和"(())()"是完整的括号字符串，"())(", "()(" 和 ")" 是不完整的括号字符串。
# 牛牛有一个括号字符串s,现在需要在其中任意位置尽量少地添加括号,将其转化 为一个完整的括号字符串。请问牛牛至少需要添加多少个括号
def needParentheses(str):
    count = 0
    add = 0
    for i in str:
        if i == '(':
            count+=1
        elif i == ')':
            count-=1
        if count<0:
            add+=1
            count = 0
    if count > 0:
        add += count
    return add

def ans(s):
    left = 0
    right = 0

    for x in s:
        if x == '(':
            left += 1
        elif x == ')':
            if left != 0:
                left -= 1
            else:
                right += 1
    res = left + right
    return res
if __name__ == '__main__':
    str = "(()(()"
    print(needParentheses(str))
    print(ans(str))