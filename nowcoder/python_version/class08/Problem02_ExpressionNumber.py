# 给定一个只由 0(假)、1(真)、&(逻辑与)、|(逻辑或)和^(异或)五种字符组成 的字符串express，再给定一个布尔值 desired。返回express能有多少种组合 方式，可以达到desired的结果。
# 【举例】
# express="1^0|0|1"，desired=false
# 只有 1^((0|0)|1)和 1^(0|(0|1))的组合可以得到 false，返回 2。 express="1"，desired=false
# 无组合则可以得到false，返回0

# 先进行有效性检查 首先字符串长度要是奇数 0 2 4 6...位置上要是0 or 1 然后奇数位置上要是逻辑符号
# 为了简化 先假设 每一个逻辑符号都是&  e.g.0&1&0&1&0 先找出最后的运算符号 对于每一个符号 都试 其左右有多少种可以出desired
# 然后加起来
# F(L,R,D) -> left right desired 递归 但很麻烦
# 还能改动态规划！
# 先做第一种方法 递归 完成了 情况很多但是不难理解
# 接下来做动态规划

def isValid(exp):
    if len(exp) & 1 == 0:
        return False
    for i in range(0,len(exp),2):
        if exp[i] != '1' and exp[i] != '0':
            return False

    for i in range(1,len(exp),2):
        if exp[i]!='&' and exp[i]!='|' and exp[i]!='^':
            return False
    return True

def p(exp, left, right, desired):

    if not isValid(exp):
        return
    if left == right:
        if exp[left] == '1':
            if desired == True:
                return 1
            else:
                return 0
        elif exp[left] == '0':
            if desired == False:
                return 1
            else:
                return 0


    res = 0
    if desired: # True
        for i in range(left+1, right , 2):
            if exp[i] == '&':
                res += p(exp, left,i-1, True) * p(exp, i+1, right, True)
            elif exp[i] == '|':
                res+= p(exp, left, i-1, True) * p(exp, i+1, right, True)
                res += p(exp, left, i - 1, True) * p(exp, i + 1, right, False)
                res += p(exp, left, i - 1, False) * p(exp, i + 1, right, True)
            elif exp[i] == '^':
                res += p(exp, left, i - 1, True) * p(exp, i + 1, right, False)
                res += p(exp, left, i - 1, False) * p(exp, i + 1, right, True)
    else:
        for i in range(left+1, right , 2):
            if exp[i] == '&':
                res += p(exp, left, i - 1, True) * p(exp, i + 1, right, False)
                res += p(exp, left, i - 1, False) * p(exp, i + 1, right, True)
                res += p(exp, left,i-1, False) * p(exp, i+1, right, False)
            elif exp[i] == '|':
                res+= p(exp, left, i-1, False) * p(exp, i+1, right, False)

            elif exp[i] == '^':
                res += p(exp, left, i - 1, True) * p(exp, i + 1, right, True)
                res += p(exp, left, i - 1, False) * p(exp, i + 1, right, False)
    return res

def method1(express, desired):
    return p(express, 0, len(express) - 1, desired)

if __name__ == '__main__':
    express = "1^0&0|1&1^0&0^1|0|1&1"
    # express = "1&1"
    print(isValid(express))

    res = method1(express, True)
    print(res)