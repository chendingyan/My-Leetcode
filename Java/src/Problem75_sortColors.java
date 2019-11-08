public class Problem75_sortColors {
    public static void sortColors(int[] nums) {
        int i  = 0;
        int j = nums.length-1;
        int cur = 0;
        while (cur <= j){
            if(nums[cur] == 0){
                swap(nums, i, cur);
                i++;
                cur++;
            }else if(nums[cur] == 2){
                swap(nums, j, cur);
                j--;
                //注意这里不需要cur++
                // 因为前面一个if里 cur左边的元素都被扫描过了 不需要验证
                // 这里换过来的元素还需要验证
            }else {
                cur++;
            }
        }
        helper.printArr(nums);
    }
    private static void swap(int []nums, int i, int j){
        if(i == j) return;
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        int [] nums = new int [] {1,2,0};
        sortColors(nums);
    }
}
