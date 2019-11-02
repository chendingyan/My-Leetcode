public class Problem23_mergeKSortedListed {

    public static ListNode mergeKLists(ListNode[] lists) {
        if (lists==null || lists.length == 0){
            return null;
        }
        return merge(lists,0, lists.length-1);
    }

    public static ListNode merge(ListNode[] lists, int left, int right){
        if(left==right){
            return lists[left];
        }
        int mid = (left+right)/2;
        ListNode l1= merge(lists, left, mid);
        ListNode l2 = merge(lists,mid+1, right);
        return mergeTwoLists(l1,l2);
    }


    public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
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
