from heapq import heappush, heappop

def heapsort(list):
    h =[]
    for i in list:
        heappush(h,i)
    list = [heappop(h) for i in range(len(h))]
    return list


def main():
    list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(heapsort(list))

if __name__ == "__main__":
    main()