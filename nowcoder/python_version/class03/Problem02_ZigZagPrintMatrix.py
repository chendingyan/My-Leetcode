# 用zigzag的方式打印矩阵，比如如下的矩阵
# 0 1 2  3
# 4 5 6  7
# 8 9 10 11
# 打印顺序为:0 1 4 8 5 2 3 6 9 10 7 11

def ZigZagPrint(matrix):
    ax = 0
    ay = 0
    bx = 0
    by = 0
    width = len(matrix[0])
    height = len(matrix)
    revert = False
    while ax != height :
        printLine(matrix, ax, ay, bx, by, revert)
        if ay < width - 1:
            ay +=1
        elif ax <= height -1:
            ax +=1

        if bx < height-1:
            bx+=1
        elif by <= width -1:
            by +=1
        revert= not revert



# 假设 上面的点叫 a 下面的点叫 b， 先从上面的点print到下面的点
def printLine(matrix, ax, ay, bx, by, revert):
    if revert == True:
        while ax <= bx and ay >= by:
            a = matrix[ax][ay]
            print(a)
            ax+=1
            ay-=1
    else:
        while ax <= bx and ay >= by:
            a = matrix[bx][by]
            print(a)
            bx-=1
            by+=1

if __name__ == '__main__':
    matrix = [
        [0,1,2,3],
        [4,5,6,7],
        [8,9,10,11]
    ]
    # printLine(matrix,0,2,2,0,False)
    ZigZagPrint(matrix)