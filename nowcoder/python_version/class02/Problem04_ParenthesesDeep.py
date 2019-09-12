# 一个合法的括号匹配序列有以下定义:
# 1空串""是一个合法的括号匹配序列 2如果"X"和"Y"都是合法的括号匹配序列,"XY"也是一个合法的括号匹配序列 3如果"X"是一个合法的括号匹配序列,那么"(X)"也是一个合法的括号匹配序列 4每个合法的括号序列都可以由以上规则生成。
# 例如: "","()","()()","((()))"都是合法的括号序列 对于一个合法的括号序列我们又有以下定义它的深度:
# 1空串""的深度是0 2如果字符串"X"的深度是x,字符串"Y"的深度是y,那么字符串"XY"的深度为 max(x,y) 3、如果"X"的深度是x,那么字符串"(X)"的深度是x+1
# 例如: "()()()"的深度是1,"((()))"的深度是3。牛牛现在给你一个合法的括号 序列,需要你计算出其深度
def ParDeep(str):
    count = 0
    maxcount = 0
    for i in str:
        if i == '(':
            count+=1
        if i == ')':
            count-=1
        if count > maxcount:
            maxcount = count
    return maxcount


# 新问题 那么如果给一个可能合法可能非法的字符串 求其子串之中 深度最长的长度
# 看到子串，看到子数组的大套路——想每个位置开头会怎么怎么样，每个位置结尾会怎么怎么样。
# str = ')(()))()()(())' =》 8


def longestValid(str):
    dp = [0] * len(str)

    for i in range(0, len(str)):
        if str[i] == '(':
            dp[i] = 0
        elif str[i] == ')':
            if i == 0:
                dp[i] = 0
            elif str[i-1] == '(':
                dp[i] = 2
                if i-2 >= 0 and dp[i-2] != 0:
                    dp[i] += dp[i-2]

            elif str[i-1] == ')':
                if str[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] +2
                    if i - dp[i] >= 0 and dp[i- dp[i]] != 0:
                        dp[i] += dp[i- dp[i]]
    print(dp)

if __name__ == '__main__':
    str = '((()))'
    print(ParDeep(str))
    str = ')(()))()()(())'
    longestValid(str)