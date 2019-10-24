package classes.class07;

public class Problem05_CompleteTreeNodeNumber {
    public static class Node {
        public int value;
        public Node left;
        public Node right;

        public Node(int data) {
            this.value = data;
            this.left = null;
            this.right = null;
        }
    }

    public static int nodeNum(Node head){
        if (head == null) {
            return 0;
        }
        int level = mostLeftLevel(head);
        if (level == 1){
            return 1;
        }
        if(level == mostLeftLevel(head.right)+ 1){
            return (int)Math.pow(2,level-1)+ nodeNum(head.right);
        }

        if(level == mostLeftLevel(head.right) + 2) {
            return (int)Math.pow(2,level-2) + nodeNum(head.left);
        }
        return -1;
    }

    public static int mostLeftLevel(Node node){
        int depth = 0;
        while(node!=null){
            depth++;
            node = node.left;
        }
        return depth;
    }

    public static Node getLastNode(Node head){
        if (head == null){
            return null;
        }
        int level = mostLeftLevel(head);
        if (level == 1){
            return head;
        }
        if(level == mostLeftLevel(head.right)+ 1){
            return getLastNode(head.right);
        }

        if(level == mostLeftLevel(head.right) + 2) {
            return getLastNode(head.left);
        }
        return null;

    }

    public static void main(String[] args) {
        Node head = new Node(1);
        head.left = new Node(2);
        head.right = new Node(3);
        head.left.left = new Node(4);
        head.left.right = new Node(5);
        head.right.left = new Node(6);
        System.out.println(nodeNum(head));
        Node res = getLastNode(head);
        System.out.println(res.value);


    }
}
