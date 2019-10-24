package classes.class07;

public class Problem02_PrintNoInArray {
    public static void printNumberNoInArray(int [] arr){
        for(int i = 0; i < arr.length; i++){
            while (arr[arr[i]-1] != arr[i]){
                //这个地方 arr[i] 交换 到后面 要用temp 细节不要出错了
                int temp = arr[i];
                arr[i] = arr[arr[i]-1];
                arr[temp-1] = temp;
            }

        }

        for(int i = 0; i < arr.length; i++){
            if(arr[i]!= i+1){
                System.out.println(i+1);
            }
        }
    }

    public static void printArr(int [] arr){
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] test = { 3, 2, 3, 5, 6, 1, 6 };
        printNumberNoInArray(test);
    }
}
