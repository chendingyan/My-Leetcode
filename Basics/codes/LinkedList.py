# LinkedList
# 链表基础知识点 长的样子
# 复杂度: insert at head, remove at head 都是O(1)
# insert at tail在有尾指针的时候也是O(1), 但 remove at tail需要O(n)
# SinglyLinkedList and DoublyLinkedList
# SinCycLinkedList
# To implement LinkedList, we need first to define Node

class SingleNode(object):
    """单个节点"""
    def __init__(self, item):
        # 表元素
        self.item = item
        # 指向下一节的链接
        self.next = None

class SinglyLinkList(object):
    """单链表"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def getLength(self):
        count = 0
        cur = self.head
        while cur != None:
            count+=1
            cur = cur.next
        return count

    def traversal(self):
        cur = self.head
        while cur != None:
            print(cur.item, end=' ')
            cur = cur.next
        print(' ')

    def insert_at_head(self, item):
        node = SingleNode(item)
        cur = self.head
        self.head = node
        node.next = cur



    def insert_at_tail(self, item):
        node = SingleNode(item)
        if self.is_empty():
            self.head = node
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = node
        node.next = None

    def insert_at_pos(self, item, pos):
        if pos <= 0:
            self.insert_at_head(item)
        elif pos >= self.getLength():
            self.insert_at_tail(item)
        else:
            node = SingleNode(item)
            cur = self.head
            while pos != 1:
                cur = cur.next
                pos-=1
            next = cur.next
            cur.next = node
            node.next = next

    def remove_at_head(self):
        next = self.head.next
        self.head = next

    def remove_item(self, item):
        cur = self.head
        if cur.item == item:
            self.remove_at_head()
        else:
            while cur.item != item:
                pre = cur
                cur = cur.next
            next = cur.next
            pre.next = next

    def search_item(self, item):
        cur = self.head
        while cur.item != item:
            cur = cur.next
            if cur == None:
                return False
        return True


def main():
    link_list = SinglyLinkList()
    print(link_list.is_empty())
    print(link_list.getLength())
    link_list.insert_at_head(2)
    print(link_list.getLength())
    link_list.insert_at_head(1)
    link_list.insert_at_tail(4)
    link_list.insert_at_pos(3,1)
    link_list.traversal()
    link_list.remove_at_head()
    link_list.traversal()
    link_list.remove_item(4)
    link_list.traversal()
    print(link_list.search_item(2))

if __name__ == '__main__':
    main()





