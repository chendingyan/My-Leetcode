# Manacher算法解决的问题
# 字符串str中，最长回文子串的长度如何求解? 如何做到时间复杂度O(N)完成?

# 回文直径 以一个位置为中心 往两边扩 扩出来区域的范围 #b#a#b# = 7 回文半径 4
# 回文直径 数组
# int R #1#2#2#1#.... 一开始R=-1 表示最右回文右边界在-1位置
# 然后 扩到0位置 R=0 扩到1位置 左右两边都能扩 此时R = 2
# int C 中心 和R是个伴随的概念 就是达到R的直径中心

# 过程 遍历字符串 每次位置i 然后又两种情况1）i在R外 2）i在R内 第一种情况无加速 第二种情况有加速
# i在R内 L i' c i R 会有三种不同情况 要看i'的回文直径在L的外面 还是里面 还是压线

def Manacher(str):
    str = addSharp(str)
    res = [0] * len(str)
    R = -1
    C = -1
    max_r = -1
    for i in range(0, len(str)):
        # i在R外
        if R < i:
            res[i] = 1
        # i在R内 R-i 是一种情况 i' = 2*C-i是另一种情况 但可以合并写
        else:
            res[i] = min(R-i, res[2*C-i])
        while i + res[i] < len(res) and i- res[i] >-1:
            if str[i+res[i]] == str[i-res[i]]:
                res[i]+=1
            else:
                break
        if i+res[i] > R:
            R = i + res[i]
            C = i
        max_r = max(max_r, res[i])
    return max_r-1


def addSharp(str):
    res = [None] * (len(str)*2+1)
    for i in range(len(res)):
        if i & 1 == 0:
            res[i] = '#'
        else:
            res[i] = str[int(i/2)]
    return res



def Manacher2(str):
    str = addSharp(str)
    pArr = [0] * len(str)
    R = -1
    C = -1
    max_r = -1
    for i in range(len(str)):
        if i > R:
            pArr[i] = 1
        else:
            pArr[i] = min(R-i, pArr[2*C-i])
        while i + pArr[i] < len(str) and i-pArr[i] > -1:
            if str[i+ pArr[i]] == str[i - pArr[i]]:
                pArr[i] +=1
            else:
                break

        if i + pArr[i] > R:
            R = i + pArr[i]
            C = i
        max_r = max(max_r, pArr[i])
    return max_r - 1

if __name__ == '__main__':
    str = 'abcscbaabbbbaaaabbbbaabcs'
    print(addSharp(str))
    print(Manacher(str))
    print(Manacher2(str))