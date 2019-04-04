# Two Pointer方法
# https://www.youtube.com/watch?v=2LjNzbK2cmA

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        leftMax = 0
        rightMax = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                res += (leftMax - height[left])
                left+=1
            else:
                rightMax = max(rightMax, height[right])
                res += (rightMax - height[right])
                right-=1
        return res