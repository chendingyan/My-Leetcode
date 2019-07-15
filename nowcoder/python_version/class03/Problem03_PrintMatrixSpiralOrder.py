# 用螺旋的方式打印矩阵，比如如下的矩阵
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 打印顺序为:0 1 2 3 7 11 10 9 8 4 5 6
# 之前我用了旋转的方法打印
# 这一次用一下宏观的思想
def PrintMatrixSpiralOrder(matrix):
    ax = 0
    ay = 0
    bx = len(matrix) - 1
    by = len(matrix[0]) - 1
    while ax <= bx or ay <= by:
        printSquare(matrix, ax, ay, bx, by)
        ax += 1
        ay += 1
        bx -= 1
        by -= 1


def printSquare(matrix, ax, ay, bx, by):
    if ax == bx:
        for i in range(ay, by + 1):
            print(matrix[ax][i], end=' ')
    elif ay == by:
        for i in range(ax, bx + 1):
            print(matrix[i][ay], end=' ')
    else:
        for i in range(ay, by):
            print(matrix[ax][i], end=' ')
        for i in range(ax, bx):
            print(matrix[i][by], end=' ')
        for i in range(by, ay, -1):
            print(matrix[bx][i], end=' ')
        for i in range(bx, ax, -1):
            print(matrix[i][ay], end=' ')


if __name__ == '__main__':
    matrix = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ]
    # printSquare(matrix,0,0,2,3)
    # printSquare(matrix,1,1,1,2)
    PrintMatrixSpiralOrder(matrix)
