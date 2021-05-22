# 首先，讲解 Next Greater Number 的原始问题：给你一个数组，返回一个等长的数组，对应索引存储着下一个更大元素，如果没有更大的元素，就存 -1。不好用语言解释清楚，直接上一个例子：
#
#
#
# 给你一个数组 [2,1,2,4,3]，你返回数组 [4,2,4,-1,-1]。
from collections import deque


def nextGreaterElement(nums):
    stack = []
    res = nums.copy()
    for i in range(len(nums) - 1, -1, -1):
        while len(stack) > 0 and stack[-1] <= nums[i]:
            stack.pop()
        if len(stack) == 0:
            res[i] = -1
        else:
            res[i] = stack[-1]
        stack.append(nums[i])
    print(res)


# 给你一个数组 T = [73, 74, 75, 71, 69, 72, 76, 73]，这个数组存放的是近几天的天气气温。你返回一个数组，计算：对于每一天，你还要至少等多少天才能等到一个更暖和的气温；如果等不到那一天，填 0 。
#
#
#
# 举例：给你 T = [73, 74, 75, 71, 69, 72, 76, 73]，你返回 [1, 1, 4, 2, 1, 1, 0, 0]。

def nextWarmerDay(nums):
    stack = deque()
    res = nums.copy()
    for i in range(len(nums) - 1, -1, -1):
        while len(stack) > 0 and nums[stack[-1]] <= nums[i]:
            stack.pop()
        if len(stack) == 0:
            res[i] = 0
        else:
            res[i] = stack[-1] - i
        stack.append(i)
    print(res)


if __name__ == '__main__':
    nums = [2, 1, 2, 4, 3]
    nextGreaterElement(nums)
    nums = [73, 74, 75, 71, 69, 72, 76, 73]
    nextWarmerDay(nums)
