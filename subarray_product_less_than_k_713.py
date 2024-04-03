class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        count = 0
        prod = 1
        left = 0
        
        for right, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[left]
                left += 1
            count += right - left + 1
        
        return count






sol = Solution()
res = sol.numSubarrayProductLessThanK([10,5,2,6], 100)
print(res)
