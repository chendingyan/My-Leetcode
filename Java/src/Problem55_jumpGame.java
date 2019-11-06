public class Problem55_jumpGame {
    public static boolean canJump(int[] nums) {
        int furtherpos = 0;
        for (int i = 0; i < nums.length-1; i++){
            if(i > furtherpos){
                return false;
            }
            if(i + nums[i] > furtherpos){
                furtherpos =i + nums[i];
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int [] nums = new int []{2,3,1,1,4};
        System.out.println(canJump(nums));
    }
}
