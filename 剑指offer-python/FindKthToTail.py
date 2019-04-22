# -*- coding:utf-8 -*-'
#  输入一个链表，输出该链表中倒数第k个结点。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        length = 0
        list = [head]
        while head:
            head = head.next
            list.append(head)
            length+=1
        if k > length:
            return None
        return list[length-k]
    def FindKthToTail2(self, head, k):
        p1 = head
        p2 = head
        while p2 and k>0:
            p2 = p2.next
            k-=1
        if k != 0:
            return None
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
        return p1
