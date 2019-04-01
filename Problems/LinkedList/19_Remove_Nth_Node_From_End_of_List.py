# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 这个问题可以用一个非常巧妙的方法来进行解决，即设立两个指针p1和p2，一开始它们都指向队首，然后单独令p2向后跳n+1个元素，这样p1和p2之间就相隔了n个元素，
# 此时令p1和p2同时向后不断跳，直到p2越过队尾（变为空），由于此时p1和p2之间相隔n个元素，所以p1的下一个元素就是我们要删除的元素了。


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next

        pre = slow
        slow = slow.next
        nex = slow.next
        pre.next = nex

        return head