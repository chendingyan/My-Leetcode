# 给一个包含n个整数元素的集合a，一个包含m个整数元素的集合b。
# 定义magic操作为，从一个集合中取出一个元素，放到另一个集合里，且操作过后每个集合的平均值都大于操作前。
# 注意以下两点:
# 1)不可以把一个集合的元素取空，这样就没有平均值了
# 2)值为x的元素从集合b取出放入集合a，但集合a中已经有值为x的元素，则a的 平均值不变(因为集合元素不会重复)，b的平均值可能会改变(因为x被取出 了)
# 问最多可以进行多少次magic操作?
# 业务分析题

# 假设两个集合 A集合一定大于B集合
# 那么这个操作一定是从A中拿出一个元素到B里面才行
# 如果A拿出一个元素x 首先这个元素不能比A的平均值大 要在 B<x<A 且这个元素 如果在B中有的话要大于B的平均值

def MagicOp(a,b):
    magic = 0
    if calculateAvg(a) < calculateAvg(b):
        temp = a
        a = b
        b = temp
    a.sort()
    b.sort()
    a_avg = calculateAvg(a)
    b_avg = calculateAvg(b)
    print(a, b)
    print(a_avg, b_avg)
    for i in range(0,len(a)):
        if a[i]<a_avg and a[i] > b_avg:
            if (a[i] in b and a[i]>b_avg) or a[i] not in b:
                magic+=1
    return magic
def calculateAvg(set):
    sum = 0
    for i in set:
        sum+=i
    return sum/len(set)

if __name__ == '__main__':
    a = [2,3,1]
    b = [1,3,4,6,2,5,8,11]

    print(MagicOp(a, b))