class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num
        
        return -1






sol = Solution()
res = sol.pivotIndex([1,7,3,6,5,6])
print(res)
