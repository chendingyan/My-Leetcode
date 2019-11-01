import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Problem17_PhoneNumberCombination {
    static Map<Character, String> phone = new HashMap<Character, String>() {{
        put('2', "abc");
        put('3', "def");
        put('4', "ghi");
        put('5', "jkl");
        put('6', "mno");
        put('7', "pqrs");
        put('8', "tuv");
        put('9', "wxyz");
    }};

    static List<String> list = new ArrayList<>();
    public static List<String> letterCombinations(String digits) {

        if(digits.length() == 0){
            return list;
        }
        process("", digits);
        return list;
    }

    public static void process(String a, String b){


        if(b.length() == 0){
            list.add(a);
            return;
        }
        char num = b.charAt(0);
        b = b.substring(1);

        String alp = phone.get(num);
        for(int i = 0; i < alp.length(); i++){
            char c = alp.charAt(i);
            process(a+c, b);
        }
    }

    public static void main(String[] args) {
        String digits = "";

        List<String> list =letterCombinations(digits);
        System.out.println(list);
    }
}
