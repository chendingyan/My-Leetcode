package classes.class07;

public class Problem07_LongestIncreasingSubsequence {
    public static int dp_way(int [] arr){
        int [] dp = new int[arr.length];
        dp[0] = 1;
        for(int i = 1; i < dp.length; i++){
            int premax = 0;
            for(int j = 0; j < i; j++){
                if (arr[j] < arr[i]){
                    premax = Math.max(dp[j] , premax);
                }
            }
            dp[i] = premax+1;
        }
        printArr(dp);
        return dp[arr.length-1];
    }

    public static int smarter_way(int [] arr){
        int [] ends = new int[arr.length];
        int [] dp = new int[arr.length];
        int size = 0;

        for(int i = 0; i < arr.length; i++){
            int left = 0;
            int right = size;
            int mid = 0;
            while (left <= right){
                mid = (left + right)/2;
                if(arr[i] <= ends[mid]){
                    right = mid -1;
                }else if(arr[i] > ends[mid]){
                    left = mid + 1;
                }
            }
            size = Math.max(size, left);
            ends[left] = arr[i];
            dp[i] = size;
        }
        printArr(dp);
        return dp[arr.length-1];
    }

    public static void printArr(int [] arr){
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int [] arr = {4,1,6,2,5,4,5,9,2,4,8,11,23,13};
        dp_way(arr);
        System.out.println(smarter_way(arr));
    }
}
