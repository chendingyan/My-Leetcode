# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 
# 
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 100] 内 
#  0 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。） 
#  Related Topics 递归 链表 
#  👍 977 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyhead = ListNode(0)
        dummyhead.next = head
        current = dummyhead
        while current.next and current.next.next:
            next = current.next
            next_next_next = next.next.next
            current.next = current.next.next
            current.next.next = next
            current.next.next.next = next_next_next
            current = current.next.next
        return dummyhead.next

# leetcode submit region end(Prohibit modification and deletion)
