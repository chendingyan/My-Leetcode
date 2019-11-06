import java.util.*;

public class Problem49_groupAnagrams {
    public static List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, List> map = new HashMap<>();
        List<List<String>> result = new ArrayList<>();
        for (String s : strs){
            int [] count = new int[26];
            Arrays.fill(count,0);
            char [] array = s.toCharArray();
            for(char c : array){
                count[c-'a']++;
            }
            StringBuilder sb = new StringBuilder("");
            for(int i = 0; i < 26;i++){
                sb.append(count[i]);
            }

            String key = sb.toString();
            System.out.println(key);
            if(!map.containsKey(key)){
                map.put(key, new ArrayList());
            }
            map.get(key).add(s);

        }
        for(List<String> v : map.values()){
            result.add(v);
        }
        return result;
    }

    public static void main(String[] args) {
        String [] strs = new String[]{"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println(groupAnagrams(strs));
    }
}
