# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。 
# 
#  子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序
# 列。 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2500 
#  -104 <= nums[i] <= 104 
#  
# 
#  
# 
#  进阶：
# 
#  
#  你可以设计时间复杂度为 O(n2) 的解决方案吗？ 
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗? 
#  
#  Related Topics 二分查找 动态规划 
#  👍 1621 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums):
        dp_list = [1] * len(nums)
        for i in range(0, len(dp_list)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp_list[i] = max(dp_list[j] + 1, dp_list[i])
        return max(dp_list)


# leetcode submit region end(Prohibit modification and deletion)


class BinarySearchSolution:
    def lengthOfLIS(self, nums):
        top = [0] * len(nums)
        piles = 0
        for num in nums:
            left = 0
            right = piles
            while left < right:
                mid = int(left + (right - left) / 2)
                if top[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            if left == piles:
                piles += 1
            top[left] = num
            print(top)


if __name__ == '__main__':
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [7, 7, 7, 7, 7, 7, 7]
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    # nums = [1,2,3]
    sol = Solution()

    sol = BinarySearchSolution()
    print(sol.lengthOfLIS(nums))
