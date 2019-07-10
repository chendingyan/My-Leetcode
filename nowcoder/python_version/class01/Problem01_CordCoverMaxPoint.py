#给定一个有序数组arr，代表数轴上从左到右有n个点arr[0]、arr[1]...arr[n-1]， 给定一个正数L，代表一根长度为L的绳子，求绳子最多能覆盖其中的几个点。


def maxPoint(array, l):
    start = 0
    end = 0
    maxPoint = 0
    while end < len(array):
        if array[end] - array[start] > l:
            temp = end - start
            if temp > maxPoint:
                maxPoint = temp
            start+=1
        else:
            end+=1

    return maxPoint



if __name__ == '__main__':
    array = [0, 13, 24, 35, 46, 57, 60, 72, 87]
    for l in range(0,20):
        print(l,maxPoint(array, l))