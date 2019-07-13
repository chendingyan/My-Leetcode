# 请编写一个程序，对一个栈里的整型数据，按升序进行排序(即排序前，栈里
# 的数据是无序的，排序后最大元素位于栈顶)，要求最多只能使用一个额外的
# 栈存放临时数据，但不得将元素复制到别的数据结构中。
def StackSortStack(stack1):
    temp = 0
    stack2 = []
    while stack1:
        temp = stack1.pop()
        print('temp = ', temp)
        while stack2!=[] and stack2[-1] > temp:
            stack1.append(stack2.pop())
        stack2.append(temp)

        print(stack1, stack2)
    print(stack2)

if __name__ == '__main__':
    stack1 = [4,1,-1,3,2,6]
    StackSortStack(stack1)
