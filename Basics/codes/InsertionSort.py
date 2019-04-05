def InsertionSort(l):
    for j in range(1, len(l)):
        temp = l[j]
        i = j
        while i > 0 and l[i-1]> temp:
            l[i] = l[i-1]
            i-=1
        l[i] = temp
    print(l)

def main():
    l = ['3','5','1','2','4','-1']
    InsertionSort(l)


if __name__ == '__main__':
    main()

# 这里要提到insertion sort的复杂度 如果是already sorted 是best case， no shift
# 如果是worst case 就是刚好反序， 那就是O(n^2)