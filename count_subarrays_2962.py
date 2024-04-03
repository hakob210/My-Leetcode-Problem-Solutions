class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        max_int = max(nums)
        count = 0
        window_start = 0

        for window_end in range(len(nums)):
            if nums[window_end] == max_int:
                count += 1

            while count >= k:
                res += len(nums) - window_end
                if nums[window_start] == max_int:
                    count -= 1
                window_start += 1

        return res






sol = Solution()
res = sol.countSubarrays([1,3,2,3,3], 2)
print(res)
