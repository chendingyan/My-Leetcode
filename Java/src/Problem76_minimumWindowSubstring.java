import java.util.HashMap;

public class Problem76_minimumWindowSubstring {
    public static String minWindow(String s, String t) {
        if (s.length() == 0 || t.length() == 0) {
            return "";
        }
        HashMap<Character, Integer> t_map = new HashMap<>();

        for (char c : t.toCharArray()){
            int count = t_map.getOrDefault(c, 0);
            t_map.put(c, count+1);
        }

        int valid_alpha = t_map.size();

        HashMap<Character, Integer> s_map = new HashMap<>();
        int [] ans = new int[]{-1, 0, 0};
        int left = 0;
        int right = 0;
        int cur_scan = 0;
        while (right < s.length()){
            char c = s.charAt(right);
            int count = s_map.getOrDefault(c, 0);
            s_map.put(c, count+1);

            if(t_map.containsKey(c) && s_map.get(c).intValue() == t_map.get(c).intValue()){
                cur_scan++;
            }
            while (left <= right && cur_scan == valid_alpha){
                c = s.charAt(left);
                if(ans[0] == -1 || ans[0] > right - left +1){
                    ans[0] = right - left+1;
                    ans[1] = left;
                    ans[2] = right;
                }

                s_map.put(c, s_map.get(c)-1);
                if(t_map.containsKey(c) && s_map.get(c).intValue() < t_map.get(c).intValue()){
                    cur_scan--;
                }
                left++;
            }
            right++;

        }
        return ans[0] == -1 ? "" : s.substring(ans[1], ans[2] + 1);
    }

    public static void main(String[] args) {
        String s = "ADOBECODEBANC";
        String t = "ABC";
        System.out.println(minWindow(s,t));
    }
}
