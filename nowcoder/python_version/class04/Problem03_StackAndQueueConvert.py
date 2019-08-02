# 如何仅用队列结构实现栈结构? 如何仅用栈结构实现队列结构?
# 问题不难 stack做queue 要两个stack 记得动态的保持两个原则 同理queue做stack

class MyQueue:
    def __init__(self):
        self.push = []
        self.pop = []

    def enqueue(self, num):
        self.push.append(num)

    def dequeue(self):
        if self.pop != []:
            return self.pop.pop()
        else:
            while self.push != []:
                self.pop.append(self.push.pop())
            return self.pop.pop()

    def print(self):
        print(self.push, self.pop)

class MyStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, num):
        if self.queue1 == []:
            self.queue2.append(num)

        if self.queue2 == []:
            self.queue1.append(num)

    def pop(self):
        if self.queue1 == []:
            while len(self.queue2) != 1:
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()

        elif self.queue2 == []:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()

    def print(self):
        print(self.queue1, self.queue2)
def testQueue():
    queue = MyQueue()
    for i in range(1,6):
        queue.enqueue(i)
    queue.print()
    print(queue.dequeue())
    queue.print()
    print(queue.dequeue())
    queue.print()
    queue.enqueue(100)
    queue.print()
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

def testStack():
    stack = MyStack()
    for i in range(1,6):
        stack.push(i)

    print(stack.pop())
    stack.print()
    print(stack.pop())
    stack.print()
    stack.push(100)
    print(stack.pop())
    stack.print()


if __name__ == '__main__':
    testStack()