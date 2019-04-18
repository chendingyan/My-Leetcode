# -*- coding:utf-8 -*-
# 输入两个链表，找出它们的第一个公共结点。
# 注意，这里的公告结点的意思是相同的点，不仅值相同，next也相同，那么同理公共结点后面的点也是不仅值相同，而且next也相同，这样的话，就可以把两条链条看成Y字型了，某一个结点后面的点全部一样。
# 举例，1->2->3->4->6和2->3->5->4->6，4就是他们的第一个公共结点。
# 那怎么求呢，有两种思路。
# 第一种就是把全部结点分别压入两个栈，利用栈的特性LIFO，然后同时pop出栈，一开始两边的元素肯定是相同的，当遇到不同的元素时，肯定已经遇到了最后一个节点，那就break
# 第二种就是分别从链表的头结点开始遍历，当两条链表有长度差时，先让长链表走他们的差值，当走到还剩下和短链表一样长时，两个链表同时遍历，这样就能找到第一个公共结点了
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next

        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if node1 != node2:
                break
        if not stack1:
            return p1
        if not stack2:
            return p2
        return node1.next