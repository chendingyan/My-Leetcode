# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。 
# 
#  当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。 
# 
#  请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。 
# 
#  注意：不允许旋转信封。 
#  
# 
#  示例 1： 
# 
#  
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。 
# 
#  示例 2： 
# 
#  
# 输入：envelopes = [[1,1],[1,1],[1,1]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= envelopes.length <= 5000 
#  envelopes[i].length == 2 
#  1 <= wi, hi <= 104 
#  
#  Related Topics 二分查找 动态规划 
#  👍 526 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        envelopes_heights = [i[1] for i in envelopes]
        return self.longest_increasing_sequence(envelopes_heights)

    def longest_increasing_sequence(self, nums):
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
                    left = mid+1
            if left == piles:
                piles += 1
            top[left] = num
        return piles


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    sol = Solution()
    sol.maxEnvelopes(envelopes)
