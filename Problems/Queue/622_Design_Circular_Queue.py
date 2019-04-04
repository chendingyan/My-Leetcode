class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.items = [None]*k
        self.head = 0
        self.tail = 0
        self.length = k
        self.size = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """

        if self.size == self.length:
            return False
        self.items[self.tail] = value
        self.size += 1
        if self.tail == self.length-1:
            self.tail = 0
        else:
            self.tail += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size == 0:
            return False
        self.items[self.head] = None
        self.size-=1
        if self.head == self.length-1:
            self.head = 0
        else:
            self.head+=1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.items[self.head]
        else:
            return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if not self.isEmpty():
            return self.items[self.tail-1]
        else:
            return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0


    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.length

def main():
    # Your MyCircularQueue object will be instantiated and called as such:
    #
    # ["MyCircularQueue", "enQueue", "Rear", "Rear", "deQueue", "enQueue", "Rear", "deQueue", "Front", "deQueue",
    #  "deQueue", "deQueue"]
    # [[6], [6], [], [], [], [5], [], [], [], [], [], []]
    k = 6
    obj = MyCircularQueue(k)
    obj.enQueue(6)
    print(obj.Rear())
    print(obj.Rear())
    obj.deQueue()
    obj.enQueue(5)
    print(obj.Rear())
    obj.deQueue()
    print(obj.Front())



if __name__ == '__main__':
    main()