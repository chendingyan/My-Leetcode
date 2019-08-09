class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        p = 1
        for i in range(0, len(nums)):
            output.append(p)
            p = p* nums[i]

        temp = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * temp
            temp = temp * nums[i]
        return output
if __name__ == '__main__':
    nums = [1,2,3,4]
    sol = Solution()
    output = sol.productExceptSelf(nums)
    print(output)