import java.util.HashMap;
import java.util.Stack;

public class Problem20_ValidParentheses {


    public boolean isValid(String s) {
        HashMap<Character, Character> map = new HashMap<>();
        map.put('{', '}');
        map.put('(', ')');
        map.put('[', ']');
        Stack<Character> stack = new Stack<>();
        for(int i =0; i < s.length();i++){
            char c = s.charAt(i);
            if(map.containsKey(c)){
                stack.add(c);
            }else if(stack.isEmpty() ||map.get(stack.pop()) != c){
                return false;
            }

        }
        return stack.isEmpty();
    }
}
