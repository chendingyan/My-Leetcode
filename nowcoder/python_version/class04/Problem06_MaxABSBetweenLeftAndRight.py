# 给定一个数组arr长度为N，你可以把任意长度大于0且小于N的前缀作为左部分，剩下的 作为右部分。
# 但是每种划分下都有左部分的最大值和右部分的最大值，请返回最大的， 左部分最大值减去右部分最大值的绝对值。
def maxABS(arr):
    max_num = max(arr)
    return max_num - min(arr[0], arr[-1])

if __name__ == '__main__':
    arr = [4,2,1,5,9,2,3,5,8,3,2,2]
    print(maxABS(arr))