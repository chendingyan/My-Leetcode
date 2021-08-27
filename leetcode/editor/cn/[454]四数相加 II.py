# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[
# l] = 0。 
# 
#  为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最
# 终结果不会超过 231 - 1 。 
# 
#  例如: 
# 
#  
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# 输出:
# 2
# 
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#  
#  Related Topics 数组 哈希表 
#  👍 391 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash_table = {}
        for i in nums1:
            for j in nums2:
                if i + j not in hash_table.keys():
                    hash_table[i + j] = 1
                else:
                    hash_table[i + j] += 1
        count = 0
        for i in nums3:
            for j in nums4:
                remain = 0 - i - j
                if remain in hash_table.keys():
                    count += hash_table[remain]
        return count
# leetcode submit region end(Prohibit modification and deletion)
