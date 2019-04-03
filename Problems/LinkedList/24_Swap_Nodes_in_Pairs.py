# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 本题相对比较简单，就是交换相邻两个元素的位置，可以使用遍历法和递归法两种方法，递归法使用两个指针记录当前要交换位置的节点，
# 在使用另外一个指针记录他们前面的那个节点。这样就可以很方便的实现节点位置的交换，然后在给三个指针更新值即可。
# 递归的写法就更简洁了，实际上利用了回溯的思想，递归遍历到链表末尾，然后先交换末尾两个，然后依次往前交换：
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        else:
            nextnode = head.next
            head.next = self.swapPairs(head.next.next)
            nextnode.next = head
            return nextnode

# 以上是一种方法
# 还有一种是设置一个虚拟头结点dummyHead
#
# 设置需要交换的两个节点分别为node1、node2，同时设置node2的下一个节点next
#
# 在这一轮操作中
# 将node2节点的next设置为node1节点
#
# 将node1节点的next设置为next节点
#
# 将dummyHead节点的next设置为node2
#
# 结束本轮操作
# 这里需要重点注意的是 设置dummyhead的时候 进入while循环内部的 要是它的一个reference 即设置另一个变量p
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyhead = ListNode(0)
        dummyhead.next = head
        p = dummyhead
        while p.next and p.next.next:
            node1 = p.next
            node2 = node1.next
            nextnode = node2.next
            node2.next = node1
            node1.next = nextnode
            p.next = node2
            p = node1

        return dummyhead.next