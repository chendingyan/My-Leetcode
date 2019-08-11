# 最长递增子序列问题
# 经典解法 O(n^2) ->O(nlogn)
def EnvelopesProblem1(arr):
    dp = [0 for i in range(len(arr))]
    dp[0] = 1
    for i in range(0, len(arr)):
        premax = 0
        for j in range(0,i):
           if arr[i] > arr[j]:
               premax = max(premax, dp[j])
        dp[i] = premax + 1

    print(dp)

# O(nlogn)解法 一个dp数组 一个ends数组 ends[i]表示 所有长度为i+1的子序列中结尾 最小的数字 dp还是表示扫描到arr[i]位置 目前最长子序列

def EnvelopesProblem2(arr):
    ends = [None for i in range(len(arr))]
    size = 0
    for x in arr:
        i = 0
        j = size
        while i != j:
            m = (i + j)//2
            if x > ends[m]:
                i = i+1
            else:
                j = m
        ends[i] = x
        size = max(i+1, size)
    print(ends, size)
    return size

if __name__ == '__main__':
    arr = [4,1,6,2,5,4,5]
    # EnvelopesProblem1(arr)
    EnvelopesProblem2([3,4,7,2,5])