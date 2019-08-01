# 实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素 的操作。
# 要求:1.pop、push、getMin操作的时间复杂度都是O(1);2.设计的栈类型可以 使用现成的栈结构

class specialStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, num):
        self.stack.append(num)
        if len(self.min) == 0:
            self.min.append(num)
            return
        current = self.min[-1]
        if num < current:
            self.min.append(num)
        else:
            self.min.append(current)

    def pop(self):
        if self.stack != []:
            num = self.stack.pop(-1)
            if num == self.min[-1]:
                self.min.pop(-1)
            return num

    def getMin(self):
        return self.min.pop(-1)

if __name__ == '__main__':
    stack = specialStack()
    stack.push(6)
    stack.push(9)
    stack.push(4)
    stack.push(2)
    stack.push(10)
    print(stack.getMin())
    print(stack.pop())
    print(stack.getMin())
    print(stack.pop())
    print(stack.getMin())


