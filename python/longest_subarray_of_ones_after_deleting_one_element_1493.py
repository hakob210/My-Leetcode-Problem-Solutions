class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        current_length = 0
        zero_index = -1

        for i, num in enumerate(nums):
            if num == 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = i - zero_index - 1
                zero_index = i

        max_length = max(max_length, current_length)

        if max_length == len(nums):
            return max_length - 1

        return max_length



sol = Solution()
res = sol.longestSubarray([1, 1, 0, 1])
print(res)
