# 给定一个正方形矩阵，只用有限几个变量，实现矩阵中每个位置的数顺时针转动90度，比如如下的矩阵
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 12 13 14 15
# 矩阵应该被调整为:
# 12 8 4 0
# 13 9 5 1
# 14 10 6 2
# 15 11 7 3
# 一条边一条边写 或者对应写要O(n^2) 而且要一个额外空间 怎么在O(1)里面做这道题？

def RotateMatrix(matrix):
    ax = 0
    ay = 0
    bx = len(matrix) -1
    by = bx
    while ax < bx:
        RotateEdge(matrix,ax,ay,bx,by)
        ax+=1
        ay+=1
        bx-=1
        by-=1

def RotateEdge(matrix, ax, ay, bx, by):
    for i in range(ay,by):
        temp = matrix[ax][ay+i]
        matrix[ax][ay + i] = matrix[bx - i][ay]
        matrix[bx - i][ay] = matrix[bx][by - i]
        matrix[bx][by - i] = matrix[ax + i][by]
        matrix[ax + i][by] = temp



def printMatrix(matrix):
    for i in matrix:
        print(i)




if __name__ == '__main__':
    matrix = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ]
    RotateMatrix(matrix)
    printMatrix(matrix)