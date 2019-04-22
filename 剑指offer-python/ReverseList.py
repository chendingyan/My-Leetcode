# -*- coding:utf-8 -*-
# 输入一个链表，反转链表后，输出新链表的表头。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        head = None
        while pHead:
            temp = ListNode(pHead.val)
            temp.next = head
            head = temp
            pHead = pHead.next
        return head