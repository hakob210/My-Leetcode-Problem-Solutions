class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                if non_zero_index != i:
                    nums[i] = 0
                non_zero_index += 1

        return nums






sol = Solution()
res1 = sol.moveZeroes([0, 1, 0, 3, 12])
res2 = sol.moveZeroes([0, 0, 1])
print(res1, res2)
