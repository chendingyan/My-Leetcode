# 给定一个N*N的矩阵matrix，只有0和1两种值，返回边框全是1的最大正方形的边 长长度。
# 例如:
# 01111
# 01001
# 01001
# 01111
# 01011 其中边框全是1的最大正方形的大小为4*4，所以返回4。

def maxBoarderSize(matrix):
    row = len(matrix)
    col = len(matrix[0])
    down = [([0] * col) for i in range(row)]
    right = [[0]*col for i in range(row)]

    for i in range(0,row):
        for j in range(0,col):
            tempi = i
            tempj = j
            temp = 0

            while tempi < row and matrix[tempi][j] == 1:
                temp+=1
                tempi+=1
            down[i][j] = temp
            temp = 0
            while tempj < col and matrix[i][tempj] == 1:
                temp+=1
                tempj+=1
            right[i][j] = temp
    print(down)
    print(right)
    maxBoarder = 0
    for i in range(0,row):
        for j in range(0,col):
            temp = min(down[i][j], right[i][j])
            if temp > maxBoarder:
                maxBoarder = temp
    return maxBoarder




if __name__ == '__main__':
    matrix = [[0,1,1,1,1],
              [0,1,0,0,1],
              [0,1,0,0,1],
              [0,1,1,1,1],
              [0,1,0,1,1],
              [0,0,0,0,0]]
    # matrix = [[1,1,0],
    #           [1,1,0],
    #           [1,1,0]]

    print(maxBoarderSize(matrix))