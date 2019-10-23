package classes.class06;

public class Problem06_SubArrayMaxSum {

    public static int maxSum(int [] arr){
        int cur = 0;
        int maxCur = 0;

        for (int i = 0; i < arr.length; i++){
            cur+= arr[i];
            if(cur < 0){
                cur = 0;
            }
            maxCur = Math.max(maxCur, cur);
        }
        return maxCur;
    }

    public static void main(String[] args) {
        int [] arr = {1,1,-1,-10,11,4,-6,9,20,-10,-2};
        System.out.println(maxSum(arr));
    }
}
