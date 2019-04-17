# -*- coding:utf-8 -*-
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# 我们把数据压入第一个栈，此时我们很清楚它的出战顺序是与我们想要的队列的出队顺序是相反的，
# 如果再把这个栈里面的元素依次压入第二个栈，此时我们想想栈2里面的元素的顺序，相当于对一组数据进行了两次倒序
class Solution:
    stack1 = []
    stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1 != []:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

        # return xx

sol = Solution()
sol.push(1)
sol.push(2)
sol.push(3)
print(sol.pop())
print(sol.pop())
sol.push(4)
print(sol.stack1)
print(sol.stack2)
print(sol.pop())
print(sol.stack1)
print(sol.stack2)
sol.push(5)
print(sol.pop())
print(sol.pop())
