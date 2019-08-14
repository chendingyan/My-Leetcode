# 岛问题
# 【题目】
# 一个矩阵中只有0和1两种值，每个位置都可以和自己的上、下、左、右 四个位置相连，如 果有一片1连在一起，这个部分叫做一个岛，求一个矩阵中有多少个岛?
# 【举例】
# 001010
# 111010
# 100100
# 000000
# 这个矩阵中有三个岛
# 【进阶】
# 如何设计一个并行算法解决这个问题

# 写一个递归 遇到一个1 把上下左右的1 都改一遍 比如改成2 visit一遍
def island(matrix):
    island = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            island += process(matrix,i,j)

    print(matrix, island)
def process(matrix, i, j):
    if matrix[i][j] == "1":
        matrix[i][j] = "2"
        process(matrix, i, j+1)
        process(matrix, i, j-1)
        process(matrix, i+1, j)
        process(matrix, i-1, j)
        return 1
    return 0


if __name__ == '__main__':
    matrix = [[0,0,1,0,1,0],
              [1,1,1,0,1,0],
              [1,0,0,1,0,0],
              [0,0,0,0,0,0]]
    matrix2 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    island(matrix2)

# 接下来进阶 如果地图很大 单cpu跑会很慢 如果有多个cpu 怎么设计并行算法