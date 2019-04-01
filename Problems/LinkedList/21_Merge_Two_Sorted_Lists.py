# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 两个链表的合并算是一个非常基本的操作，为了达到最快的时间复杂度和最优的空间复杂度，我们应当尽量少的进行冗余的操作。

# 所以在求解答案的过程中，我们首先考虑答案的第一个元素——毋庸置疑的，一定是第一个链表的最小值（即第一个元素）和第二个链表的最小值（第一个元素）中的较小值，
# 于是我们将其从对应的链表中删去并放置进答案链表中。

# 此时问题的规模缩小了1，变成了在总长度减少了1的两个链表中寻找一个最小的元素，再将其放置进答案链表的末端。

# 依次类推，直到两个链表均为空，便可以得到我们想要求解的答案。

# 需要注意的是，在一个链表为空的时候，在判断两个链表中的最小值时需要进行特殊的判断。
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head1 = l1
        head2 = l2
        result = ListNode(0)
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        if head1.val < head2.val:
            result = head1
            result.next = self.mergeTwoLists(head1.next, head2)
        else:
            result = head2
            result.next = self.mergeTwoLists(head2.next, head1)

        return result
