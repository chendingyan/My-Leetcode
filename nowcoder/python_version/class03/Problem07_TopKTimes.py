# 给定一个字符串类型的数组arr，求其中出现次数最多的前K个
# 这个题很关键
# 做法是hashmap统计 再加到一个大小为K的heap中 在python的实现中我们可以自己写一个heap实现加node

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return str(self.key) +':'+ str(self.value)

class MyHeap:
    def __init__(self, k):
        self.k = k
        self.data = []

    def size(self):
        return len(self.data)

    def push(self, key, value):
        node = Node(key, value)
        if self.size() < self.k:
            self.data.append(node)
            self.uphead(len(self.data)- 1)

        else:
            self.data[0] = node
            self.downheap(0)


    def uphead(self, pos):
        if self.data[pos] < self.data[pos//2] and pos >= 0:
            self.data[pos], self.data[pos//2] = self.data[pos//2], self.data[pos]
            self.uphead(pos//2)

    def downheap(self, pos):
        if pos * 2 < len(self.data)-1:
            leftchild = self.data[pos*2]
            smallest = pos * 2
            if pos *2 +1 < len(self.data)-1:
                rightchild = self.data[pos*2+1]
                if rightchild < leftchild:
                    smallest = pos*2+1
            if self.data[smallest] < self.data[pos]:
                self.data[smallest], self.data[pos] = self.data[pos], self.data[smallest]
                self.downheap(smallest)

    def print(self):
        for i in self.data:
            print(str(i))


def topKtimes(arr,k):
    hash = dict()
    for i in arr:
        if i not in hash.keys():
            hash[i] = 1
        else:
            hash[i]+=1
    print(hash)

    myheap = MyHeap(k)
    for i in hash.items():
        myheap.push(i[0], i[1])
    myheap.print()



if __name__ == '__main__':
    # arr = [1,2,2,2,1,2,3,3,5,5,6,7,3,3,2,1,4,5,6,7,1,2,3,4,2,1,6,6,6,6,6]
    arr = ['a','a','a','b','b','b','b','c','c','d','d','d','d','d','d','e','e']
    topKtimes(arr, 4)
