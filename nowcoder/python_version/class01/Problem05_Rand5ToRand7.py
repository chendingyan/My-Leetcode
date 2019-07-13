# 给定一个函数f，可以1~5的数字等概率返回一个。请加工出1~7的数字等概率 返回一个的函数g。
# 给定一个函数f，可以a~b的数字等概率返回一个。请加工出c~d的数字等概率 返回一个的函数g。
# 给定一个函数f，以p概率返回0，以1-p概率返回1。请加工出等概率返回0和1的 函数g
import random


def rand5():
    return random.randint(1, 5)

def rand2():
    if rand5() == 1 or rand5() == 2:
        return 0
    elif rand5() == 4 or rand5() == 5:
        return 1
    else:
        return rand2()
def rand7():
    while True:
        num = (rand5()-1) * 5 + rand5()-1
        if num <= 20:
            break
    return int(num%7)+1


if __name__ == '__main__':
    count1 = 0
    for i in range(10000):
        if rand7() == 1:
            count1+=1
    print(count1)
