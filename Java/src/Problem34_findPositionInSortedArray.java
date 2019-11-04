import java.util.HashMap;

public class Problem34_findPositionInSortedArray {

    //最基本的二分查找框架

    public int binary_search(int [] nums, int target){
        int start = 0;
        int end = nums.length-1;
        int mid = 0;
        while(start <= end){
            mid = start+(end-start)/2;
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] > target){
                end = mid -1;
            }else if (nums[mid] < target) {
                start = mid + 1;
            }
        }
        return -1;
    }

//    此算法有什么缺陷？
//
//    答：至此，你应该已经掌握了该算法的所有细节，以及这样处理的原因。但是，这个算法存在局限性。
//
//    比如说给你有序数组 nums = [1,2,2,2,3]，target = 2，此算法返回的索引是 2，没错。但是如果我想得到 target 的左侧边界，即索引 1，或者我想得到 target 的右侧边界，即索引 3，这样的话此算法是无法处理的。
//
//    这样的需求很常见。你也许会说，找到一个 target，然后向左或向右线性搜索不行吗？可以，但是不好，因为这样难以保证二分查找对数级的复杂度了。


    public static int left_bound(int[] nums, int target){
        int start = 0;
        int end = nums.length;
        int mid = 0;
        while(start < end){
            mid = start + (end-start)/2;
            if(nums[mid] == target){
                end = mid;
            }else if(nums[mid] > target){
                end = mid;
            }else if (nums[mid] < target) {
                start = mid+1;
            }
        }
        if(end == nums.length){
            return -1;
        }
        return nums[end] == target? end: -1;
    }

    public static int right_bound(int [] nums, int target){
        int start = 0;
        int end = nums.length;
        int mid = 0;
        while(start< end){
            mid = start + (end-start)/2;
            if(nums[mid] == target){
                start = mid+1;
            }else if(nums[mid] > target){
                end = mid;
            }else if (nums[mid] < target) {
                start = mid+1;
            }
        }
        if(end == 0){
            return -1;
        }
        return nums[end-1] == target? end-1: -1;
    }


    public static int[] searchRange(int[] nums, int target) {
        int [] res = {left_bound(nums, target), right_bound(nums, target)};
        return res;
    }

    public static void main(String[] args) {
        int [] nums ={5,7,7,8,8,10};
        int [] res = searchRange(nums, 8);
        System.out.println(res[0]+" "+ res[1]);

    }
}
