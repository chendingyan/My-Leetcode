# 给定一个元素为非负整数的二维数组matrix，每行和每列都是从小到大有序的。 再给定一个非负整数aim，请判断aim是否在matrix中。
def FindNum(matrix, num):
    i = len(matrix[0])-1
    j = 0
    while i >= 0 and j < len(matrix):
        if matrix[i][j] > num:
            i-=1
        elif matrix[i][j]< num:
            j+=1
        elif matrix[i][j] == num:
            return True
    return False

if __name__ == '__main__':
    matrix = [
        [1,2,14,22],
        [4,5,16,23],
        [6,7,20,26],
        [19,20,25,44]
    ]
    print(FindNum(matrix, 24))