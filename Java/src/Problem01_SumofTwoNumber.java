import java.util.HashMap;
import java.util.Map;

//这道题是要用哈希问题 hashmap
public class Problem01_SumofTwoNumber {
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length ; i++){
            int complement = target - nums[i];
            if (map.containsKey(complement)){
                int index2 = map.get(complement);
                int [] res = new int[]{index2, i};
                return res;
            }
            map.put(nums[i], i);
        }
        return null;
    }

    public static void main(String[] args) {
        int[]nums = new int[]{2,7,11,13} ;
        int target = 9;
        int [] res = twoSum(nums, target);
        System.out.println(res[0]+" " + res[1]);
    }
}
