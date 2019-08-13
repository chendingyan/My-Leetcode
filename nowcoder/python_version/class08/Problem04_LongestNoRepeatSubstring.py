# 在一个字符串中找到没有重复字符子串中最长的长度。
# 例如:
# abcabcbb没有重复字符的最长子串是abc，长度为3 bbbbb，答案是b，长度为1
# pwwkew，答案是wke，长度是3
# 要求:答案必须是子串，"pwke" 是一个子字符序列但不是一个子字符串。

# 面对这种字符子串的题目 需要想的是以某个字符开头 如何 以某个字符结尾 如何
# 对于这题 我们考虑每个字符结尾 如果i位置结尾 我们要看字符的上一次出现的位置 如果上次出现 比i-1的最长无重复子串还左边 那加上i位置
# 否则就是 从上一次出现位置+1 到现在

def LongestNoRepeat(str):
    ans = 0
    dp = 1
    map = dict()
    map[str[0]] = 0
    max_pos = 0
    for i in range(1, len(str)):
        if str[i] not in map:
            map[str[i]] = i
            dp +=1

        else:
            pre_pos = map[str[i]]
            if pre_pos < i - dp:
                dp +=1
            else:
                dp = i - pre_pos
            map[str[i]] = i
        if dp > ans:
            ans = dp
            max_pos = i
        substring = str[max_pos-ans+1:max_pos+1]
        print(ans, substring)
    return ans, substring
if __name__ == '__main__':
    str = 'wyhfqebfgenvraqitnuc'
    LongestNoRepeat(str)