def merge(left,right):
    res = []
    while left and right:
        if left[0]< right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    res = res+left+right
    return res

def mergesort(lists):
    if len(lists)<=1:
        return lists
    mid = len(lists)//2
    left = mergesort(lists[:mid])
    right = mergesort(lists[mid:])
    return merge(left, right)

def main():
    l = ['3','5','1','2','4','-1']
    lists = mergesort(l)
    print(lists)

if __name__ == '__main__':
    main()