# 给定一个数组arr，已知其中所有的值都是非负的，将这个数组看作一个容器， 请返回容器能装多少水
# 比如，arr = {3，1，2，5，2，4}，根据值画出的直方图就是容器形状，该容 器可以装下5格水
# 再比如，arr = {4，5，1，3，2}，该容器可以装下2格水

def waterproblem(arr):
    left = arr.copy()
    right = arr.copy()
    for i in range(1, len(arr)):
        left[i] = max(left[i-1], arr[i])

    for i in range(len(arr)-2, -1, -1):
        right[i] = max(right[i+1], arr[i] )
    print(left, right)
    sum = 0
    for i in range(1, len(arr)-1):
        sum+= min(left[i], right[i]) - arr[i]
    print(sum)
waterproblem([4,5,1,3,2])