import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Problem94_binaryTreeInorderTraversal {
    public static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> inorder = new ArrayList<>();
        helper(root, inorder);
        return inorder;
    }
    public static void helper(TreeNode root, List<Integer> inorder){
        if(root == null) return;
        if(root.left!= null){
            helper(root.left, inorder);
        }

        inorder.add(root.val);
        if(root.right != null){
            helper(root.right, inorder);
        }

    }
    public static List<Integer> inorderTraversal2(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> inorder = new ArrayList<>();
        if(root == null) return new ArrayList<>();
        while (!stack.isEmpty() || root!=null){
            if(root!=null){
                stack.push(root);
                root = root.left;
            }else {
                root = stack.pop();
                inorder.add(root.val);
                root = root.right;
            }
        }
        return inorder;
    }


    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(2);
        root.right.left = new TreeNode(3);
        List<Integer> inorder = inorderTraversal(root);
        System.out.println(inorder);

    }
}
