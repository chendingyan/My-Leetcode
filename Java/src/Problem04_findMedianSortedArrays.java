// 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
// 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
// 你可以假设 nums1 和 nums2 不会同时为空。
public class Problem04_findMedianSortedArrays {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
//        if (n > m){
//            findMedianSortedArrays(nums2, nums1);
//        }
        if (m == 0) {
            if (n % 2 == 0) {
                return (nums2[n / 2 - 1] + nums2[n / 2]) / 2.0;
            } else {

                return nums2[n / 2];
            }
        }
        if (n == 0) {
            if (m % 2 == 0) {
                return (nums1[m / 2 - 1] + nums1[m / 2]) / 2.0;
            } else {
                return nums1[m / 2];
            }
        }



        int LMax1 = 0,LMax2 = 0, RMin1 = 0, RMin2=0, c1=0, c2 = 0;
        int lo = 0;
        int hi = 2*n;

        while (lo <= hi){
            c1 = (lo + hi)/2;
            c2 = m + n - c1;

            LMax1 = (c1 == 0)? Integer.MIN_VALUE: nums1[(c1-1)/2];
            RMin1 = (c1 == 2* n)? Integer.MAX_VALUE: nums1[(c1/2)];
            LMax2 = (c2== 0)? Integer.MIN_VALUE: nums2[(c2-1)/2];
            RMin2 = (c2 == 2* n)? Integer.MAX_VALUE: nums2[(c2/2)];

            if (LMax1 > RMin2){
                hi = c1 - 1;
            }
            else if (LMax2 > RMin1){
                lo = c1 + 1;
            }
            else{
                break;
            }
        }
        return (Math.max(LMax1, LMax2) + Math.min(RMin1, RMin2)  )/2.0;
    }

    public static void main(String[] args) {
        int [] nums1 = new int[]{2};
        int [] nums2 = new int[]{};
        double res = findMedianSortedArrays(nums1, nums2);
        System.out.println(res);
    }
}
