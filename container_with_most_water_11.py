class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area




sol = Solution()
res = sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(res)
