# 如果一个字符串为str，把字符串str前面任意的部分挪到后面形成的字符串叫 作str的旋转词。
# 比如str="12345"，str的旋转词有"12345"、"23451"、 "34512"、"45123"和"51234"。给定两个字符串a和b，请判断a和b是否互为旋转 词。
# 比如: a="cdab"，b="abcd"，返回true。 a="1ab2"，b="ab12"，返回false。 a="2ab1"，b="ab12"，返回true。

# trick的方法 用到string matching里面的KMP算法

def easypython(a,b):
    a = a + a
    if b in a:
        return True
    return False

def gen_pnext(substring):
    m = len(substring)
    pnext = [0] * m
    index = 0
    i = 1
    while i < m:
        if substring[i] == substring[index]:
            pnext[i] = index+1
            i+=1
            index+=1
        elif index!=0:
            index = pnext[index-1]
        else:
            pnext[i] = 0
            i+=1
    return pnext

def kmp(a,b):
    a = a + a
    pnext = gen_pnext(b)
    n = len(a)
    m = len(b)
    i,j = 0,0
    while i < n and j < m:
        if a[i] == b[j]:
            i+=1
            j+=1
        elif j!=0:
            j = pnext[j-1]
        else:
            i+=1
    if j == m:
        return True
    return False


if __name__ == '__main__':
    a = "cdab"
    b = "abcd"
    print(easypython(a,b))
    print(kmp(a,b))