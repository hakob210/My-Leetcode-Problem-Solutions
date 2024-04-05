class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
    def maxOperations(self, nums, k):
        nums.sort()
        l = 0
        h = len(nums) - 1
        count = 0
        while l < h:
            total = nums[l] + nums[h]
            if total == k:
                count += 1
                l += 1
                h -= 1
            elif total < k:
                l += 1
            else:
                h -= 1
        return count









sol = Solution()
res = sol.maxOperations([1, 2, 3, 4], 5)
print(res)
