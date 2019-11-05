import java.util.ArrayList;
import java.util.List;

public class Problem46_Permutation {
    public static List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        int [] visited = new int [nums.length];
        helper(nums, visited, result, list);
        System.out.println(result);
        return result;
    }

    public static void helper(int [] nums, int[] visited, List<List<Integer>> result,List<Integer> list){
        if (list.size() == nums.length){
            result.add(new ArrayList<>(list));
        }
        for(int i = 0; i < nums.length; i++){
            if(visited[i] == 1){
                continue;
            }
            visited[i] = 1;
            list.add(nums[i]);
            helper(nums, visited, result, list);
            visited[i] = 0;
            list.remove(list.size()-1);
        }
    }

    public static void main(String[] args) {
        int [] nums = {1,2,3};
        permute(nums);
    }
}
