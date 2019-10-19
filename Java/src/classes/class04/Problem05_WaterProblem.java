package classes.class04;
//基本的方法是 对于每一个位置 能放多少水 那么要看左边最大值 右边最大值的最小值 和目前位置的高度的差值

public class Problem05_WaterProblem {
    public static int waterProblem1(int [] arr){
        //第一种 方法 用预处理数组
        int [] leftMax = new int[arr.length];
        int [] rightMax = new int[arr.length];
        leftMax[0] = arr[0];
        for (int i = 1; i < arr.length; i++){
            leftMax[i] = Math.max(arr[i], leftMax[i-1]);
        }

        rightMax[arr.length-1] = arr[arr.length-1];
        for(int i = arr.length-2; i > -1; i--){
            rightMax[i] = Math.max(arr[i], rightMax[i+1]);
        }

        printArr(leftMax);
        printArr(rightMax);
        int water = 0;
        for(int i = 1; i < arr.length-1; i++){
            water += Math.min(leftMax[i],rightMax[i])- arr[i];
        }
        return water;
    }


    public static void printArr(int [] arr){
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int [] arr = {3,1,2,5,2,4};
        System.out.println(waterProblem1(arr));
    }

}
