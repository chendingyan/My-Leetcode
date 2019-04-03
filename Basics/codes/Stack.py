class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isempty(self):
        return self.size() == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[self.size()-1]

    def traversal(self):
        print(self.items)
def main():
    mystack = Stack()
    mystack.push(1)
    mystack.push(2)
    mystack.traversal()
    print(mystack.pop())
    mystack.traversal()

if __name__ == '__main__':
    main()
