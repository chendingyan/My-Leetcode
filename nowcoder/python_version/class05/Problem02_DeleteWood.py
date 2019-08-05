# 在迷迷糊糊的大草原上，小红捡到了n根木棍，第i根木棍的长度为i，
# 小红现在很开心。想选出其中的三根木棍组成美丽的三角形。 但是小明想捉弄小红，想去掉一些木棍，使得小红任意选三根木棍都不能组成三角形。
# 请问小明最少去掉多少根木棍呢? 给定N，返回至少去掉多少根?

# 三角形 要两边之和 大于或者等于 第三遍 也就是说一个数组 任意选3个数字 小的两个加起来不能大于或者等于 大的那个数

def deleteWood(n):
    if n < 4:
        return 0
    num1 = 1
    num2 = 2
    num = 2
    while num1 + num2 <= n:
        num +=1
        temp = num1 + num2
        num1 = num2
        num2 = temp
    return n - num

if __name__ == '__main__':
    print(deleteWood(8)) # 12358