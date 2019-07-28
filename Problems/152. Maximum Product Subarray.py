class Solution(object):
    def maxProduct(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [None]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i] , nums[i])
        print(dp)
        return max(dp)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = nums.copy()

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return max(dp)
if __name__ == '__main__':
    sol = Solution()
    A = [2,3,-2,3]
    B = [-2,1,-3,4,-1,2,1,-5,4]
    C = [2,7,9,3,1]
    # print(sol.maxProduct(A))
    # print(sol.maxSubArray(B))
    print(sol.rob(C))