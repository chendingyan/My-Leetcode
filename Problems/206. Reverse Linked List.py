# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    prev = ListNode(None)
    cur = head
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev


if __name__ == '__main__':
    head = ListNode(1)
    sec = ListNode(2)
    thr = ListNode(3)
    head.next = sec
    sec.next = thr
    head = reverseList(head)
    print(head.val, head.next.val, head.next.next.val, head.next.next.next.val)