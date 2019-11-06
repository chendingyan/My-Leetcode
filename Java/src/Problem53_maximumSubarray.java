public class Problem53_maximumSubarray {
    public static int maxSubArray(int[] nums) {
        int sum = 0;
        int max = nums[0];
        for(int i = 0; i< nums.length; i++){
            max = Math.max(nums[i], max);
        }
        if(max < 0){
            return max;
        }
        for(int i = 0; i< nums.length; i++){

            sum+= nums[i];
            if(sum < 0){
                sum = 0;
            }
            max = Math.max(max,sum);
        }
        return max;
    }

    public static void main(String[] args) {
        int [] nums = new int[] {-2,1,-3,4,-1,2,1,-5,4};
        System.out.println(maxSubArray(nums));
    }
}
