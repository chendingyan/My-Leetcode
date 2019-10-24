package classes.class07;

import java.util.Scanner;

public class Problem04_Kiki {

    public static int minCoins(int x, int y, int z, int start, int end){
        int [] dp = new int[end+1];
        dp[start] = 0;
        for(int i = 0; i < start; i++){
            dp[i] = 0;
        }
        for(int i = start+1; i < dp.length; i++){
            if(i < 2 ){
                dp[i] = Math.min(dp[i+2]+z, dp[i/2]+y);
            }else if(i < (end-1)) {
                dp[i] = Math.min(dp[i+2]+z, dp[i/2]+y);
                dp[i] = Math.min(dp[i], dp[i-2]+x);
            }else{
                dp[i] =Math.min(dp[i-2] + x, dp[i/2] + y);
            }
//            dp[i] =Math.min(dp[i-2] + x, dp[i+2]+z , dp[i/2] + y);

        }
        printArr(dp);
        return -1;
    }

    public static void printArr(int [] arr){
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
//        3 100 1 2 6
        int x = 3;
        int y = 100;
        int z = 1;
        int start = 2;
        int end = 6;
        minCoins(x,y,z,start,end);
    }
}
