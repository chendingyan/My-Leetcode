# 一堆数组 要不就是左边0右边1 要不就是全0 或者 全1 请问那个数组1最多

def extra01(matrix):
    width = len(matrix[0])
    height = len(matrix)
    i = 0
    j = width-1
    res = []
    size = 0
    while i < height and j >= 0:
        if matrix[i][j] == 1:
            if j == 0:
                if size == width:
                    res.append(i)
                else:
                    size = width
                    res = [i]
                i+=1
            else:
                j-=1
        elif matrix[i][j] == 0:
            if size < width - j-1:
                size = width - j-1
                res = [i]
            elif size == width - j-1:
                res.append(i)
            j+=1
            i+=1

    return res, size


if __name__ == '__main__':
    matrix = [
        [0,0,1,1,1,1,1],
        [0,0,0,0,0,1,1],
        [0,0,1,1,1,1,1],
        [0,0,1,1,1,1,1],
        [0,0,0,0,0,0,0]
        # [0,1,1,1,1,1,1],
        # [0, 1, 1, 1, 1, 1, 1],
        # [0, 1, 1, 1, 1, 1, 1]
    ]
    res, size = extra01(matrix)
    print(res, size)
