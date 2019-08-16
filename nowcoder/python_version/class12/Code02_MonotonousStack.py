# 在数组中想找到一个数，左边和右边比这个数小、且离这个数最近的位置。
# 如果对每一个数都想求这样的信息，能不能整体代价达到O(N)?需要使用到单调栈结构
# 单调栈结构的原理和实现


def getSmallestNoRepeat(arr):
    stack = []
    res = [[0 for i in range(2)] for i in range(len(arr))]
    for i in range(0, len(arr)):
        while len(stack)!=0 and arr[stack[-1]] > arr[i]:
            temp = stack.pop()
            if len(stack) == 0:
                left = None
            else:
                left = arr[stack[-1]]
            res[temp][0] = left
            res[temp][1] = arr[i]
        stack.append(i)
    while len(stack) != 0:
        temp = stack.pop()
        if len(stack) == 0:
            left = None
        else:
            left = arr[stack[-1]]
        res[temp][0] = left
        res[temp][1] = None
    return res

def getSmallestRepeat(arr):
    stack = []
    res = [[0 for i in range(2)] for i in range(len(arr))]
    for i in range(0, len(arr)):

        while len(stack) != 0 and arr[stack[-1][-1]] > arr[i]:
            temp = stack.pop()
            if len(stack) == 0:
                left = None
            else:
                left = arr[stack[-1][-1]]
            for j in temp:
                res[j][0] = left
                res[j][1] = arr[i]
        if len(stack) != 0 and arr[stack[-1][-1]] == arr[i]:
            stack[-1].append(i)
        else:
            stack.append([i])
    while len(stack) != 0:
        temp = stack.pop()
        if len(stack) == 0:
            left = None
        else:
            left = arr[stack[-1][-1]]
        for i in temp:
            res[i][0] = left
            res[i][1] = None
    return res
if __name__ == '__main__':
    arr = [3,4,3,3,3,2,5,1,6]
    # res = getSmallestNoRepeat(arr)
    # print(res)
    res = getSmallestRepeat(arr)
    print(res)