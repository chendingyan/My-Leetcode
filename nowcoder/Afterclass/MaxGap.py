# 给定一个长度为N(N>1)的整型数组A，可以将A划分成左右两个部分，左部分A[0..K]，右部分A[K+1..N-1]，K可以取值的范围是[0,N-2]。
# 求这么多划分方案中，左部分中的最大值减去右部分最大值的绝对值，最大是多少？
# 这一题 要利用智慧 智慧的力量赋予你
def findMaxGap(A,n):
    max_value =  max(A)
    min_side = min(A[0],A[n-1])
    return max_value-min_side

if __name__ == '__main__':
    A = [2,7,3,1,1]
    n = 5
    print(findMaxGap(A,n))