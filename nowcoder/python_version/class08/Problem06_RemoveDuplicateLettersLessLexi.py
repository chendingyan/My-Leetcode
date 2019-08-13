# 给定一个全是小写字母的字符串str，删除多余字符，使得每种字符只保留一个，并让 最终结果字符串的字典序最小
# 【举例】
# str = "acbc"，删掉第一个'c'，得到"abc"，是所有结果字符串中字典序最小的。
# str = "dbcacbca"，删掉第一个'b'、第一个'c'、第二个'c'、第二个'a'，得到"dabc"， 是所有结 果字符串中字典序最小的。

# 字典序最小 字典序就是两个字符串 从高位开始比  ASCII码 看哪个小
# 这道题 运用的是贪心策略 虽然我也不能证明这个贪心

def SubstringLexi(str):
    if not str or len(str) == 1:
        return str
    hash = dict()
    for i in str:
        if i in hash:
            hash[i] +=1
        else:
            hash[i] = 1
    break_i = 0
    min_char = str[0]
    for i in range(len(str)):
        hash[str[i]]-=1
        if hash[str[i]] == 0:
            break_i = i
            break
        else:
            if str[i] < min_char:
                min_char = str[i]
    print(min_char)
    return min_char + SubstringLexi(str[break_i:].replace(min_char,''))


if __name__ == '__main__':
    ans = SubstringLexi('dbcacbca')
    print(ans)
