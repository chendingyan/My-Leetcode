import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Problem102_binaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root == null) return new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        List<List<Integer>> anslist = new ArrayList<>();
        queue.add(root);
        while (!queue.isEmpty()){
            List<Integer> list = new ArrayList<>();
            int size = queue.size();
            for(int i = 0; i < size; i++){
                TreeNode cur = queue.poll();
                list.add(cur.val);
                if(cur.left != null){
                    queue.add(cur.left);
                }
                if(cur.right != null){
                    queue.add(cur.right);
                }
            }
            anslist.add(list);
        }
        return anslist;
    }

    public List<List<Integer>> levelOrder2(TreeNode root) {
        List<List<Integer>> anslist = new ArrayList<>();
        helper(anslist, root, 0);
        return anslist;
    }
    public static void helper(List<List<Integer>> anslist, TreeNode root, int level){
        if(root == null) return;
        if(anslist.size() == level) anslist.add(new ArrayList<>());
        anslist.get(level).add(root.val);
        helper(anslist, root.left, level+1);
        helper(anslist, root.right, level+1);

    }
}
