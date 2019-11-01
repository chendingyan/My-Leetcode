public class Problem21_mergeTwoSortedList {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode pre =head;
        while(l1 != null && l2!=null){
            if(l1.val <= l2.val){
                head.next = l1;
                head = head.next;
                l1 = l1.next;
            }else {
                head.next = l2;
                head = head.next;
                l2 = l2.next;
            }

        }
        head.next = l1==null? l2:l1;
        return pre.next;
    }
}
