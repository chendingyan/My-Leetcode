# KMP 我还是比较熟悉和自信的

# 主要是generate prefix 我们使用第一位是 -1 第二位是0 这样看前一个的实现方法
# 整体复杂度O(N)

def kmp(str1, str2):
    next = generatePrefix(str2) # O(M)
    # 底下算 str matching O(N)
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i+=1
            j+=1
        elif j > 0:
            j = next[j]
        else:
            i+=1

    if j == len(str2):
        return i - j
    else:
        return -1



def generatePrefix(str):
    if len(str) == 1:
        return [-1]
    next = [0]* len(str)
    next[0] = -1
    next[1] = 0
    i = 2
    cur = 0
    while i < len(str):
        if str[i-1] == str[cur]:
            next[i] = cur+1
            i +=1
            cur +=1
        elif cur != 0:
            cur = next[cur]
        else:
            next[i] = 0
            i+=1
    return next


if __name__ == '__main__':
    str1 = 'abcabcababaccc'
    match = 'ababa'
    next = generatePrefix(match)
    print(next)
    res = kmp(str1, match)
    print(res)
