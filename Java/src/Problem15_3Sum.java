import java.util.*;

//给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

//排序 对于每个数 找另外两个和为target的数
public class Problem15_3Sum {
    public static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for(int i = 0; i < nums.length; i++){
            if (nums[i] <= 0 && (i == 0 || nums[i]!= nums[i-1])){
                int target = -nums[i];
                System.out.println(target);
                int left = i+1;
                int right = nums.length-1;
                while (left < right){
                    int rightNum = nums[right];
                    int leftNum = nums[left];
                    if(nums[left] + nums[right] > target){

                        right--;
                        while (right > left && nums[right] == rightNum){
                            right--;
                        }


                    }else if (nums[left] + nums[right] < target){
                        left++;
                        while (left < right && nums[left] == leftNum){
                            left++;
                        }
                    }else {
                        List<Integer> list = new ArrayList<>();
                        list.add(nums[i]);
                        list.add(nums[left]);
                        list.add(nums[right]);
                        result.add(list);
                        left++;
                        while (left < right && nums[left] == leftNum){
                            left++;
                        }
                    }
                }


            }
        }
        return result;

    }

    public static void main(String[] args) {
        List<List<Integer>> result = threeSum(new int[]{0,0,0,0});
        System.out.println(result);
    }


}
