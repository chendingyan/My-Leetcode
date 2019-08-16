# 定义:数组中累积和与最小值的乘积，假设叫做指标A。
# 给定一个数组，请返回子数组中，指标A最大的值。

# 这道题不是很好想到用单调栈 我们是有一套选取规则
# 遍历arr 选取 带i位置的元素 且i位置上元素是最小值 然后它最小情况下的A 也就是 要他两边扩充到 比他大的最远 不能扩充到比他还小的地方 然后对于每个位置都取A 进行比较

# 首先 还是要实现一个单调栈
def mono_stack(arr):
    res =[[0 for _ in range(2)] for _ in range(len(arr))]
    stack = []
    for i in range(len(arr)):
        while len(stack) != 0 and arr[stack[-1][-1]] > arr[i]:
            temp = stack.pop()
            if len(stack) == 0:
                left = -1
            else:
                left = stack[-1][-1]
            for j in temp:
                res[j][0] = left
                res[j][1] = i
        if len(stack) != 0 and arr[stack[-1][-1]] == arr[i]:
            stack[-1].append(i)
        else:
            stack.append([i])
    while len(stack) != 0:
        temp = stack.pop()
        if len(stack) == 0:
            left = -1
        else:
            left = stack[-1][-1]
        for j in temp:
            res[j][0] = left
            res[j][1] = -1
    return res

def AlltimesA(arr):
    res = mono_stack(arr)
    print(res)
    A_list = [0]* len(arr)
    for i in range(len(arr)):
        left = res[i][0]
        right = res[i][1]
        if right == -1:
            right = len(arr)
        sum = 0
        for j in range(left+1, right):
            sum += arr[j]
        A_list[i] = arr[i] * sum
    print(A_list)
    return max(A_list)
if __name__ == '__main__':
    # arr = [3,4,1,3,5,2,4]
    arr = [66, 31, 63, 26, 92, 56, 9, 60, 68, 11 ]
    max = AlltimesA(arr)
    print(max) # should be 8684