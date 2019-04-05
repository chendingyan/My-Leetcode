# 升序
def BubbleSort(l):
    for i in range (1,len(l)):
        for j in range (0, i):
            if l[j] > l[j+1]:
                temp = l[j+1]
                l[j+1] = l[j]
                l[j] = temp
    print(l)

def main():
    l = ['3','5','1','2','4']
    BubbleSort(l)


if __name__ == '__main__':
    main()