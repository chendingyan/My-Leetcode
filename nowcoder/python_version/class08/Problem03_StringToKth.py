# 在数据加密和数据压缩中常需要对特殊的字符串进行编码。给定的字母表A由26个小写英文字母组成，即 A={a, b...z}。
# 该字母表产生的长序字符串是指定字符串中字母从左到右出现的次序与字母在字母表中出现 的次序相同，且每个字符最多出现1次。
# 例如，a，b，ab，bc，xyz等字符串是升序字符串。
# 对字母表A产生的所有长度不超过6的升序字符串按照字典排列编码如下:a(1)，b(2)，c(3)......，z(26)，ab(27)， ac(28)......
# 对于任意长度不超过16的升序字符串，迅速计算出它在上述字典中的编码。
# 输入描述: 第1行是一个正整数N，表示接下来共有N行，在接下来的N行中，每行给出一个字符串。输出描述: 输出N行，每行对应于一个字符串编码。
# 示例1:
# 输入
# 3
# a
# b
# ab
# 输出
# 1
# 2
# 27

# 技巧是 设置两个函数 F(N) 返回长度为N的字符串有多少个 然后有一个子函数G(char,k)代表以字符char开头长度为K的字符串的个数
# 那么F(N) = G(a,N)+G(b,N)+...+G(z,N) 那么 G怎么算？ G(a,N) = a开头 加上 G(b,N-1) + G(c,N-1)+....G(z, N-1) 递归！

def StringToKth():
    arr = []
    s = input()
    num = int(s)
    while num != 0:
        arr.append(input())
        num-=1
    print(arr)
    for i in arr:
        print(process(i))
# 第i个字符开头、长度为len的所有字符串中的第一个字符串，是第几个
def G(i,k):
    if k == 1:
        return 1
    # G(i,k) = G(i+1,k-1)+G(i+2,k-1)+...
    sum = 0
    for x in range(i+1,27):
        sum += G(x,k-1)
    return sum


def F(n):
    sum = 0
    if n == 0:
        return 0
    for i in range(1,27):
        sum += G(i,n)
    return sum

# 递归情况 很容易出错
# 首先 e.g. 'bcd'  先要加上长度为1的长度为2的 在长度为3的里 先加上 以a开头长度为3的 再确定b位置 b-c之间开头长度为2的 当然这里是0 最后 d同理
def process(str):
    sum = 0
    for i in range(1,len(str)):
        sum += F(i)
    pre = 0
    for i in range(0, len(str)):
        num = ord(str[i]) - ord('a')+ 1

        for j in range(pre+1, num):
            sum+=G(j,len(str) - i)
        pre = num
    return sum + 1
if __name__ == '__main__':
    # StringToKth()
    print(process('d'))