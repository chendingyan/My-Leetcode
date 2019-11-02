public class Problem31_nextPermutation {
    public static void nextPermutation(int[] nums) {
        for(int i = nums.length-1; i>0;i--){
            if(nums[i] > nums[i-1]){
                //这个位置比他前一个位置大
                int pivot = nums[i-1];
                int minmax = 0;
                for(int j = i; j < nums.length; j++){
                    if(nums[j] > pivot){
                        minmax = j;
                    }
                }
                nums[i-1] = nums[minmax];
                nums[minmax] = pivot;
                reverse(nums, i, nums.length-1);
                return;
            }
        }
        reverse(nums, 0, nums.length-1);
        printArr(nums);
        return;
    }

    public static void reverse(int [] nums, int head, int rear){
        while(head < rear){
            int temp = nums[head];
            nums[head] = nums[rear];
            nums[rear] = temp;
            head++;
            rear--;
        }
        return;
    }

    public static void printArr(int [] arr){
        for(int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int [] nums = {1,1,5};
        nextPermutation(nums);
    }
}
