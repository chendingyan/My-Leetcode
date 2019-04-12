# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
# 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 要删除有序链表中所有的重复节点，而头结点有可能就是重复节点。这样的比较好的解决方式就是新建头结点，然后往后遍历，同样的值就全部略过。

# 要注意第一个节点 如果重复 不能 return pHead
# 否则会出错
# 这道题坑特别多 包括while 为什么要有cur的检查 以及其顺序 都会影响到不同的test case
# 1）传NULL
# 2）只有一个节点
# 3）头节点开始就有重复
# 4）中间节点重复
# 5）尾部节点重复
# 6）链表中没有重复链表
# 7）所有节点都是重复的
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        last = ListNode(-1)
        last.next = pHead
        ans = last
        cur = pHead
        while cur and cur.next:
            if cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                last.next = cur
            else:
                cur = cur.next
                last = last.next
        return ans.next

    def getNewChart(self, list):
        if list:
            node = ListNode(list.pop(0))
            node.next = self.getNewChart(list)
            return node

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    list = [1,1,1]
    listNode = Solution().getNewChart(list)
    head = Solution().deleteDuplication(listNode)
    while head:
        print(head.val, end=" ")
        head = head.next
