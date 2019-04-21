# -*- coding:utf-8 -*-
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
# 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        first = path[0]
        position = [idx for idx, i in enumerate(matrix) if i==first]
        print(position)
        if position == []:
            return False
        flag = 0
        for pos in position:
            flag+=1
            print('pos'+ str(pos))
            arrived = []
            for i in path[1:]:
                if pos+1 < len(matrix) and matrix[pos+1] == i and pos+1 not in arrived:
                    print('1')
                    arrived.append(pos)
                    pos = pos+1
                elif pos-1 >=0 and matrix[pos-1] == i and pos-1 not in arrived:
                    print('2')
                    arrived.append(pos)
                    pos = pos-1
                elif pos+cols < len(matrix) and matrix[pos+cols] == i and pos+cols not in arrived:
                    print('3')
                    arrived.append(pos)
                    pos = pos+cols
                elif pos- cols >=0 and matrix[pos-cols] == i and pos-cols not in arrived:
                    print('4')
                    arrived.append(pos)
                    pos = pos - cols
                else:
                    print('zhale')
                    print('flag = '+str(flag))
                    if flag == len(position):
                        return False
                    else:
                        break
                print('arrived= ' +str(arrived))

                if len(arrived) == len(path)-1:
                    return True

        return True



list1 = 'ABCESFCSADEE'
# abce
# sfcs
# adee

matrix = []
for i in list1:
    matrix.append(i)
list2 = 'ABCB'
print(list2 in list1)
# list2 ='ABCCED'
path = []
for i in list2:
    path.append(i)
# matrix =['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e']
# path = ['a','c','c','e','d']
row = 3
cols = 4
first = path[0]

sol = Solution()
print(sol.hasPath(matrix, row, cols, path))