# -*- coding:utf-8 -*-
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        p1, p2 = pHead1, pHead2
        ret = ListNode(0)
        temp = ret
        while p1 and p2:
            if p1.val < p2.val:
                temp.next = ListNode(p1.val)
                p1 = p1.next
            else:
                temp.next = ListNode(p2.val)
                p2 = p2.next
            temp = temp.next
        if p1:
            temp.next = p1
        else:
            temp.next = p2
        return ret.next