
# 假设s和m初始化，s = "a"; m = s; 再定义两种操作，第一种操作:
# m = s;
# s = s + s;
# 第二种操作: s = s + m;
# 求最小的操作步骤数，可以将s拼接到长度等于n


# 思路：
# 实际上求的是m取得最大值最少需要几步
# 因为s一定是m的倍数
#
# 当n为质数，则只能通过步骤二来凑n
# 当n不是质数，将其拆分成各个质数，然后步骤就是每个质数的实现步骤
# 假设有n = a * b * c * d (质数因子）
# n = (a*b*c) 要弄d份 要调用d-1次操作2
# n = (a*b) * c 要弄 c-1个操作2 以此类推
# n 次数= a-1 * b-1 * c-1 * d-1 = a+b+c+d - 质数因子的个数
import math

# 第一个问题 怎么判断一个数 是不是质数
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

# 接下来第二个问题 怎么把一个数 拆分成 各个质数因子
def minOps(n):
    if n < 2:
        return 0
    if isPrime(n):
        return n-1
    sum = 0
    count = 0
    for i in range(2, n):
        while n % i == 0:
            sum+=i
            count+=1
            n/=i
    # print(sum, count)
    return sum - count

if __name__ == '__main__':
    # print(isPrime(4))
    for i in range(2,20):
        print(minOps(i))
