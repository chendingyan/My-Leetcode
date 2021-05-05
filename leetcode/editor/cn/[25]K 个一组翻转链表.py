# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。 
# 
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  进阶： 
# 
#  
#  你可以设计一个只使用常数额外空间的算法来解决此问题吗？ 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1,2,3,4,5], k = 1
# 输出：[1,2,3,4,5]
#  
# 
#  示例 4： 
# 
#  
# 输入：head = [1], k = 1
# 输出：[1]
#  
# 
#  
#  
# 
#  提示： 
# 
#  
#  列表中节点的数量在范围 sz 内 
#  1 <= sz <= 5000 
#  0 <= Node.val <= 1000 
#  1 <= k <= sz 
#  
#  Related Topics 链表 
#  👍 1076 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + str(self.next)


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        a = head
        b = head
        for i in range(k):
            if not b:
                return head
            b = b.next
        newhead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newhead

    def reverse(self, a, b):
        pre = None
        cur = a
        nxt = a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


# leetcode submit region end(Prohibit modification and deletion)


class SolutionIterative:
    # 反转区间[a, b) 的元素，注意是左闭右开
    def reverse(self, a, b):
        pre = None
        cur = a
        nxt = a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


if __name__ == '__main__':
    b = ListNode(3, ListNode(4, ListNode(5)))
    head = ListNode(1, ListNode(2, b))
    sol = SolutionIterative()
    print(sol.reverse(head, b))
