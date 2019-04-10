class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def isEmpty(self):
        return (self) == 0

    def __str__(self):
        return str(self.key) +':'+ str(self.value)


class Heap:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def add(self, key, value):
        node = Node(key, value)
        self.data.append(node)
        self.upheap(len(self.data)-1)

    def upheap(self, pos):
        if self.data[pos] < self.data[pos//2] and pos >= 0:
            self.data[pos] , self.data[pos//2] = self.data[pos//2], self.data[pos]
            self.upheap(pos//2)

    def removeMin(self):
        if self.isEmpty():
            return False
        min = self.data[0]
        last_node = self.data.pop()
        self.data[0] = last_node
        self.downheap(0)
        return str(min)

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

    def min(self):
        min = self.data[0]
        return str(min)

heap = Heap()
heap.add(4, "D")
heap.add(3, "C")
heap.add(1, "A")
heap.add(5, "E")
heap.add(2, "B")
heap.add(7, "G")
heap.add(6, "F")
heap.add(26, "Z")
for item in heap.data:
    print(item)

print("remove min: ")
print(heap.removeMin())
print("Now min is: ")
print(heap.min())
print()