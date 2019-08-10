# 给定一个整数数组A，长度为n，有 1 <= A[i] <= n，且对于[1,n]的整数，其 中部分整数会重复出现而部分不会出现。 实现算法找到[1,n]中所有未出现在A中的整数。
# 提示:尝试实现O(n)的时间复杂度和O(1)的空间复杂度(返回值不计入空间复 杂度)。
# 输入描述:
# 一行数字，全部为整数，空格分隔
# A0 A1 A2 A3...
# 输出描述:
# 一行数字，全部为整数，空格分隔R0 R1 R2 R3... 示例1:
# 输入
# 1343
# 输出
# 2

# 重点是怎么实现这个O(1)的空间复杂度
# 对于这个数组 进行换位操作 目的是让数组i位置上的num = i+1 如果最后发现不在正确位置上的 就是没有出现的数字
def PrintNotInArray(arr):
    for i in range(len(arr)):
        while arr[i]!= arr[arr[i]-1]:
            temp = arr[i]
            arr[i] = arr[arr[i]-1]
            arr[temp-1] = temp
    print(arr)

    for i in range(len(arr)):
        if arr[i] != i+1:
            print(i+1)
if __name__ == '__main__':
    arr = [1,3,4,3,8,4,2,2]
    PrintNotInArray(arr)
