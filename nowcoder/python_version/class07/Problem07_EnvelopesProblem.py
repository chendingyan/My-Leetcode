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
                i = m+1
            else:
                j = m
        ends[i] = x
        size = max(i+1, size)
    print(ends, size)
    return size

# 最后到信封问题 一个信封有两个信息 一个是长 一个是高
# 给定 好多好多的信封 如果 A的长和高都小于B 那么A信封可以被装进 B信封里面 那么给你很多个信封 可以套几层
# 这不就是一个Longest Increasing Subsequence 问题的变式吗
# 但这里有技巧 先把信封 排序 按 长度 由小到大排序 长度一样的 按高度由大到小排序
# 然后把高度数组拿出来 对高度数组 进行LIS 就是我们信封最多可以套几层 这个地方很关键 我直接拿LIS去做 是做不对这个题的 一定要这样预处理

# 那这个预处理 有什么原理呢 这就是最秀的地方 因为我们排序按 长度比我小的 在我左边  长度和我一样 高度比我大的在我左边 长度和我一样 高度比我小的在我右边
# 这样的话 我已经按长度从小到大排序了 而出现在某个X左边的 一定是 长度小 且高度也小 （我可以套的） 因为一样长度也不能算套进去 左边出现的必然是长度高度都小的
# 这样的话我对做LIS 其实 就是按高度 找到最长的递增子序列 而长度之前就已经约束了 我再约束高度 就完美了 太tmd秀了

class Envelopes:
    def __init__(self, l, h):
        self.length = l
        self.height = h
    def __lt__(self, other):
        return self.length < other.length and self.height < other.height

    def __str__(self):
        return "Length = " + str(self.length) + " Height = " + str(self.height)


from functools import cmp_to_key
def mycmp(a,b):
    if a.length != b.length:
        return a.length - b.length
    else:
        return b.height - a.height

def EnvelopesProblem3(arr):
    # sort
    # arr = sorted(arr, cmp = mycmp)

    arr.sort(key=cmp_to_key(mycmp))
    height =[]
    for i in range(len(arr)):
        height.append(arr[i].height)
        print(arr[i])
    print(height)
    # LIS 做法
    ends = [None for i in range(len(height))]
    size = 0
    for x in height:
        i = 0
        j = size
        while i != j:
            m = (i+j)//2
            if x > ends[m]:
                i = m + 1
            else:
                j = m
        ends[i] = x
        size = max(i+1, size)
    for i in ends:
        print(i)
    print(size)
    return size



if __name__ == '__main__':
    arr = [4,1,6,2,5,4,5]
    # EnvelopesProblem1(arr)
    EnvelopesProblem2([3,4,7,2,5])

    test = [[3, 4 ], [ 2, 3 ], [ 4, 5 ], [ 1, 3 ], [ 2, 2 ], [ 3, 6 ], [ 1, 2 ], [ 3, 2 ], [ 2, 4 ] ]
    arr = []
    for i in test:
        env = Envelopes(i[0], i[1])
        arr.append(env)
    EnvelopesProblem3(arr)
