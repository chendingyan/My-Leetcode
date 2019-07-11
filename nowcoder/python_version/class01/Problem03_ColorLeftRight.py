# 牛牛有一些排成一行的正方形。每个正方形已经被染成红色或者绿色。
# 牛牛现在可以选择任意一个正方形然后用这两种颜色的任意一种进行染色,这个正方形的颜色将会被覆盖。
# 牛牛的目标是在完成染色之后,每个红色R都比每个绿色G距离最左侧近。 牛牛想知道他最少需要涂染几个正方形。
# 如样例所示: s = RGRGR 我们涂染之后变成RRRGG满足要求了,涂染的个数为2,没有比这个更好的涂染方案。
# 其实目的是 把左边都变成R 右边都变成G
# 这种问题 需要遍历 但是这种遍历是重复的 可以保存一些重复遍历的字典 变成查表法
def ColorLeftRight(s):
    s = list(s)
    num_r = 0
    for i in s:
        if s == 'R':
            num_r +=1
    num_g = len(s) - num_r
    s.append('#')
    R2G = [0]*len(s)
    for i in range(len(s), 0, -1):
        if s[i-1] == 'R':
            for j in range(0,i):
                R2G[j] +=1
    print(R2G)

    G2R = [0]*len(s)
    for i in range(0, len(s)):
        if s[i] == 'G':
            for j in range(i+1, len(s)):
                G2R[j] +=1
    print(G2R)
    min_num = len(s)
    for i in range(0, len(s)):
        if R2G[i] + G2R[i] < min_num:
            min_num = R2G[i] + G2R[i]
    print(min_num)


if __name__ == '__main__':
    s = 'GGGGGR'
    ColorLeftRight(s)

