# 给定一个数组arr，如果通过调整可以做到arr中任意两个相邻的数字相乘是4的倍数， 返回true;如果不能返回false
# 分类 分为三类 1：2的倍数但不是4的倍数 2：4的倍数 3：什么也不是
# 然后讨论各种数 的数量和位置关系

# 如果没有1， 有2，3 那么2的数量可以比3的数量少一个 或者更多
# 如果有1， 那么1要两两在一起 并且连接着一个2 可以把这一堆1当做一个3
def NearMultiple4Times(arr):
    twoTimes = 0
    fourTimes = 0
    others = 0
    for i in arr:
        if i % 4 == 0:
            fourTimes+=1
        elif i % 2 == 0:
            twoTimes+=1
        else:
            others+=1
    if twoTimes == 0:
        if fourTimes >= others-1:
            return True
    else:
        if fourTimes >= others:
            return True
    return False



