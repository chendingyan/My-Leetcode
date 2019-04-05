def SelectionSort(l):
    for i in range(len(l)):
        print(i)
        pos_smallest = i
        for j in range(i, len(l)):
            if l[j] <= l[pos_smallest]:
                pos_smallest = j
        temp = l[i]
        l[i] = l[pos_smallest]
        l[pos_smallest] = temp
    print(l)


def main():
    l = ['3','5','1','2','4']
    SelectionSort(l)


if __name__ == '__main__':
    main()