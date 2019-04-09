def stdquicksort(L):
    qsort(L, 0, len(L)-1)
    return L

def qsort(L, first, last):
    if first < last:
        split = partition(L, first, last)
        qsort(L, first, split-1)
        qsort(L, split+1, last)

def partition(L, first, last):
    pivot = L[first]
    leftmark = first+1
    rightmark = last

    while True:
        while L[leftmark] <= pivot:  # 如果列表中存在与划分元素pivot相等的元素，让它位于left部分
            # 以下检测用于划分元素pivot是列表中的最大元素时，防止leftmark越界
            if leftmark == rightmark:
                break
            leftmark += 1

        while L[rightmark] > pivot:
            # 这里不需要检测，划分元素pivot是列表中的最小元素时，rightmark会自动停在first处
            rightmark -= 1

        if leftmark < rightmark:
            # 此时，leftmark处的元素大于pivot，而rightmark处的元素小于等于pivot，交换二者
            L[leftmark], L[rightmark] = L[rightmark], L[leftmark]
        else:
            break

    # 交换first处的划分元素与rightmark处的元素
    L[first], L[rightmark] = L[rightmark], L[first]

    # 返回划分元素pivot的最终位置
    return rightmark

def main():
    l = ['3','5','1','2','4','-1']
    lists = stdquicksort(l)
    print(lists)

if __name__ == '__main__':
    main()