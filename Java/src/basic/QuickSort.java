package basic;

import java.util.PriorityQueue;

public class QuickSort {

    public static void quickSort(int [] arr, int low, int high){
        if(low > high){
            return;
        }
        int index = partition(arr, low, high);
        quickSort(arr, low, index-1);
        quickSort(arr, index+1, high);
    }

    private static int partition(int [] arr, int low, int high){
        if(low > high){
            return -1;
        }
        int pivot = arr[low];

        while (low < high){
            while (low < high && arr[high] >= pivot){
                high--;
            }

            arr[low] = arr[high];

            while (low < high && arr[low] <= pivot){
                low++;
            }

            arr[high] = arr[low];

        }
        arr[low] = pivot;
        return low;


    }

    public static int findKLargest(int[] arr, int low, int high, int k){
        int index =partition(arr, low, high);
        if(index == k-1){
            return arr[index];
        }else if(index > k-1){
            return findKLargest(arr, low, index-1,k);
        }else {
            return findKLargest(arr, index+1, high,k);
        }
    }


    public static void main(String[] args) {
        int[] arr = {10,7,2,4,7,62,3,4,2,1,8,9,19};
        quickSort(arr, 0 , arr.length-1);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]  + " ");
        }
        System.out.println();
        int ans = findKLargest(arr, 0, arr.length-1, 1);
        System.out.println(ans);

    }

}
