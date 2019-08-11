# 能不能被三整除
def getNum(l, r):
    sum = 0
    for i in range(l, r+1):
        temp = float(i+1)*float(i)/float(2)
        if temp % 3 == 0:
            sum+=1
    return sum

if __name__ == '__main__':
    print(getNum(100000000,100004000))