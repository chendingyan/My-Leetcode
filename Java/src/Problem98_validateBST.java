import java.util.Stack;

public class Problem98_validateBST {
    public static boolean isValidBST(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        double pre = - Double.MAX_VALUE;
        while (root != null || !stack.isEmpty()){
            if(root!=null){
                stack.push(root);
                root = root.left;
            }else {
                root = stack.pop();
                if (pre >= root.val) return false;
                pre = root.val;
                root = root.right;
            }
        }
        return true;

    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(2);
        System.out.println(isValidBST(root));
    }
}
