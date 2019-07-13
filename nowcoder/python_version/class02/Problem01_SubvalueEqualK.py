# 给定一个数组arr，求差值为k的去重数字对。
def SubvalueEqualK(arr,k):
    dic = dict()
    for i in arr:
        i = int(i)
        dic[i] = 1
    print(dic)
    res = []
    for i in dic:
        if dic.__contains__(i+k):
            res.append((i,i+k))
    print(res)
if __name__ == '__main__':
    arr = '121111345'

    SubvalueEqualK(arr,1)