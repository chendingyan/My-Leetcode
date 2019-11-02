import java.util.ArrayList;
import java.util.List;

public class Problem22_GenerateParentheses {
    public static List<String> list = new ArrayList<>();
    public static List<String> generateParenthesis(int n) {

        helper(0,0, n , "");
        return list;
    }

    public static void helper(int left, int right, int n, String res){
        if ( left == n && right == n){
            list.add(res);
            return;
        }
        if (left < n){
            helper(left+1, right, n, res+"(");
        }
        if (left > right && right < n){
            helper(left, right+1, n, res + ")");
        }
    }

    public static void main(String[] args) {
        System.out.println(generateParenthesis(1));
    }

}
