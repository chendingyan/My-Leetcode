# 字符串只由'0'和'1'两种字符构成， 当字符串长度为1时，所有可能的字符串为"0"、"1"; 当字符串长度为2时，所有可能的字符串为"00"、"01"、"10"、"11"; 当字符串长度为3时，所有可能的字符串为"000"、"001"、"010"、"011"、"100"、 "101"、"110"、"111"
# 如果某一个字符串中，只要是出现'0'的位置，左边就靠着'1'，这样的字符串叫作达标字符串。
# 给定一个正数N，返回所有长度为N的字符串中，达标字符串的数量。 比如，N=3，返回3，因为只有"101"、"110"、"111"达标。

# 这就是一个斐波那契额数列问题 但是要注意的是 怎么把问题转化成斐波那契
# 假设f(n) 是还剩长度为n没决定 但之前的字符 必为1  这种情况下 有多少种合法的
# 如果要长度为7 因为第一位肯定是1 我们还有6个字符长度没决定 我们调用 f(6)
# 然后考虑f的递归 如果 f(6) 我们第一位又可以是1 或者0 了 如果是1 代表我们只要在合法的f(5)前加上一个1就可以了
# 如果是0 我们不能在剩下5位第一位是0 所以剩下五位第一位又是1 又回到了我们的递归 就是f(4)
# 所以f(6) = f(5) + f(4) ===> 斐波那契


# 对于斐波那契数列的解法 有一种logn 复杂度的公式


# [f(n), f(n-1)]  = [f(2), f(1)] * [a b ]  ^ (n-2)
#                                  [c d ]

# 为什么这个解法是logn 这又涉及到之中实现的问题 这个实现 有一个矩阵的指数次幂 的乘积 这个地方可以用logn来解
# 假设我们算10^75 我们先把75 转换成2进制 75 = 64+8+2+1 =  1001011
# 那么我们先算 10^1 如果二进制位上是1 我们就乘进去  如果 二进制位上是0 我们不乘进去继续 然后10^2 10^4 10^8
import numpy as np
def numPower(num, n):
    temp = num
    cur = 0
    res = 1
    while cur < n:
        if (n & (1 << cur)) != 0:
            res = res * temp
        temp = temp * temp
        cur += 1
    return res
# 4 = 100 7 = 111
# print(numPower(2,4))

def matrixPower(matrix, n):
    temp = matrix
    cur = 0
    res = [[0]* len(matrix[0]) for i in range(len(matrix))]
    for i in range(0, len(matrix)):
        res[i][i] = 1
    while cur < n:
        if (n & (1 << cur)) != 0:
            res = np.dot(res, temp)
        temp = np.dot(temp, temp)
        cur +=1
    return res

def matrixMulti(a, b):
    res = [[0] * len(b[0]) for i in range(len(a))]
    for i in range(0, len(res)):
        for j in range(0, len(res[0])):
            for k in range(0, len(b)):
                res[i][j] += (a[i][k] * b[k][j])

    return res

def fib(n):
    base = [[1,1],[1,0]]
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    temp = matrixPower(base, n-2)
    temp1 = np.dot([1,1], temp)
    return temp1[0]

if __name__ == '__main__':
    for i in range(1,10):
        print(fib(i))